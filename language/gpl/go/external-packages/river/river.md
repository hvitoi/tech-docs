# River

- Background job queue for Go backed by PostgreSQL
- <https://github.com/riverqueue/river>
- Jobs are rows in the `river_job` table, so they can be inserted in the same transaction as your business data (no lost/phantom jobs)
- Workers fetch jobs with `SELECT ... FOR UPDATE SKIP LOCKED`, so many processes can safely share one queue

## Installation

```shell
go get github.com/riverqueue/river
go get github.com/riverqueue/river/riverdriver/riverpgxv5   # driver for pgx v5
go get github.com/jackc/pgx/v5

# optional CLI (migrations, etc.)
go install github.com/riverqueue/river/cmd/river@latest
```

## Core concepts

- **JobArgs**: Struct with the job payload (JSON-serialized) + `Kind() string` identifier
- **Worker**: Type that implements `Work(ctx, *river.Job[T]) error` for one `JobArgs`
- **Workers**: Registry mapping job kinds to workers
- **Client**: Inserts jobs and (if started) runs workers for configured queues
- **Queue**: Named lane of jobs, each with its own concurrency (`MaxWorkers`)
- **Migrations**: Create River's tables (`river_job`, `river_leader`, `river_queue`, ...)

## Job lifecycle

```text
insert ──► scheduled ──(time reached)──► available ──► running ──► completed
               ▲                             ▲            │
               │                             │            ├──(error)──► retryable ──► (backoff) ──► available
               └─────── JobSnooze ───────────┼────────────┤
                                             │            ├──(JobCancel)───────────► cancelled
                                             │            └──(MaxAttempts reached)─► discarded
                                        (manual retry)
```

- Default `MaxAttempts` is 25, with exponential backoff between attempts
- `completed`, `cancelled`, `discarded` are final states (old rows are pruned automatically)

## Migrations

```shell
# CLI
river migrate-up --database-url "$DATABASE_URL"
river migrate-down --database-url "$DATABASE_URL" --max-steps 1
```

```go
// programmatic (e.g. on app startup or in tests)
migrator, err := rivermigrate.New(riverpgxv5.New(pool), nil)
_, err = migrator.Migrate(ctx, rivermigrate.DirectionUp, nil)
```

## Hands-on demo

Inserts 5 jobs covering the main behaviors (immediate, scheduled, retried, cancelled, transactional) and prints events as they finish.

### 1. Start Postgres

```shell
docker run -d --rm --name river-pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:17
export DATABASE_URL="postgres://postgres:postgres@localhost:5432/postgres"
```

### 2. Create the project

```shell
mkdir riverdemo && cd riverdemo
go mod init riverdemo
go get github.com/riverqueue/river github.com/riverqueue/river/riverdriver/riverpgxv5 github.com/jackc/pgx/v5
```

### 3. `main.go`

```go
package main

import (
    "context"
    "errors"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/jackc/pgx/v5/pgxpool"
    "github.com/riverqueue/river"
    "github.com/riverqueue/river/riverdriver/riverpgxv5"
    "github.com/riverqueue/river/rivermigrate"
)

type EmailArgs struct {
    To      string `json:"to"`
    Subject string `json:"subject"`
}

func (EmailArgs) Kind() string { return "email" }

type EmailWorker struct {
    river.WorkerDefaults[EmailArgs]
}

func (w *EmailWorker) Work(ctx context.Context, job *river.Job[EmailArgs]) error {
    if job.Args.To == "" {
        return river.JobCancel(errors.New("missing recipient"))
    }
    // Fail the first attempt to show retries in action.
    if job.Attempt == 1 && job.Args.To == "flaky@example.com" {
        return errors.New("smtp timeout")
    }
    fmt.Printf("[attempt %d] sending %q to %s\n", job.Attempt, job.Args.Subject, job.Args.To)
    return nil
}

func (w *EmailWorker) NextRetry(job *river.Job[EmailArgs]) time.Time {
    return time.Now().Add(time.Second)
}

func main() {
    ctx := context.Background()

    pool, err := pgxpool.New(ctx, os.Getenv("DATABASE_URL"))
    if err != nil {
        log.Fatal(err)
    }
    defer pool.Close()

    migrator, err := rivermigrate.New(riverpgxv5.New(pool), nil)
    if err != nil {
        log.Fatal(err)
    }
    if _, err := migrator.Migrate(ctx, rivermigrate.DirectionUp, nil); err != nil {
        log.Fatal(err)
    }

    workers := river.NewWorkers()
    river.AddWorker(workers, &EmailWorker{})

    client, err := river.NewClient(riverpgxv5.New(pool), &river.Config{
        Queues: map[string]river.QueueConfig{
            river.QueueDefault: {MaxWorkers: 10},
        },
        Workers: workers,
    })
    if err != nil {
        log.Fatal(err)
    }

    done, cancel := client.Subscribe(river.EventKindJobCompleted, river.EventKindJobCancelled)
    defer cancel()

    if err := client.Start(ctx); err != nil {
        log.Fatal(err)
    }

    // Plain insert
    if _, err := client.Insert(ctx, EmailArgs{To: "alice@example.com", Subject: "Welcome"}, nil); err != nil {
        log.Fatal(err)
    }

    // Scheduled insert
    if _, err := client.Insert(ctx, EmailArgs{To: "bob@example.com", Subject: "Reminder"}, &river.InsertOpts{
        ScheduledAt: time.Now().Add(3 * time.Second),
    }); err != nil {
        log.Fatal(err)
    }

    // Fails once, then succeeds on retry
    if _, err := client.Insert(ctx, EmailArgs{To: "flaky@example.com", Subject: "Retry me"}, nil); err != nil {
        log.Fatal(err)
    }

    // Cancelled permanently
    if _, err := client.Insert(ctx, EmailArgs{Subject: "No recipient"}, nil); err != nil {
        log.Fatal(err)
    }

    // Transactional insert: the job only exists if the tx commits
    tx, err := pool.Begin(ctx)
    if err != nil {
        log.Fatal(err)
    }
    if _, err := client.InsertTx(ctx, tx, EmailArgs{To: "carol@example.com", Subject: "Order confirmed"}, nil); err != nil {
        log.Fatal(err)
    }
    if err := tx.Commit(ctx); err != nil {
        log.Fatal(err)
    }

    for range 5 {
        ev := <-done
        fmt.Printf("event=%s job_id=%d state=%s\n", ev.Kind, ev.Job.ID, ev.Job.State)
    }

    if err := client.Stop(ctx); err != nil {
        log.Fatal(err)
    }
}
```

### 4. Run it

```shell
go run .
```

```text
[attempt 1] sending "Welcome" to alice@example.com
event=job_completed job_id=1 state=completed
[attempt 1] sending "Order confirmed" to carol@example.com
event=job_cancelled job_id=4 state=cancelled
event=job_completed job_id=5 state=completed
[attempt 2] sending "Retry me" to flaky@example.com
event=job_completed job_id=3 state=completed
[attempt 1] sending "Reminder" to bob@example.com
event=job_completed job_id=2 state=completed
```

### 5. Inspect the table

```shell
docker exec river-pg psql -U postgres -c "SELECT id, kind, state, attempt, args FROM river_job ORDER BY id"
```

```text
 id | kind  |   state   | attempt |                           args
----+-------+-----------+---------+-----------------------------------------------------------
  1 | email | completed |       1 | {"to": "alice@example.com", "subject": "Welcome"}
  2 | email | completed |       1 | {"to": "bob@example.com", "subject": "Reminder"}
  3 | email | completed |       2 | {"to": "flaky@example.com", "subject": "Retry me"}
  4 | email | cancelled |       1 | {"to": "", "subject": "No recipient"}
  5 | email | completed |       1 | {"to": "carol@example.com", "subject": "Order confirmed"}
```

### 6. Clean up

```shell
docker stop river-pg
```

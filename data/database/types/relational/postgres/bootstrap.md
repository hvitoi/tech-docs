# Bootstrap - docker-entrypoint-initdb.d

> See installation.md on how to use bootstrap files with docker

- The official `postgres` image (also `mysql`, `mongo`) runs any `*.sql`, `*.sql.gz`, `*.sh` files dropped in `/docker-entrypoint-initdb.d/` on startup, in alphabetical order
- Files are mounted in via a volume or baked in with `COPY` in a Dockerfile
- `Only runs once` — when the data directory (`$PGDATA`) is empty on first boot. If the volume already holds data, the scripts are `silently skipped`
- So editing a script and restarting does nothing; you must wipe the volume (`docker compose down -v`) to re-run

- This is `not a migration system` — it is a one-time bootstrap / seed:
  - no version tracking, no `up`/`down`, no re-running, no rollback
  - it cannot evolve an existing database — only initialise a fresh one
- Good for: local dev, CI, and seeding demo data
- For anything long-lived, run a real migration tool (Flyway, Alembic, …) against the container *after* it starts — keep `initdb.d` for the initial empty-DB bootstrap only

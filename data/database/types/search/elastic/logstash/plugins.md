# Logstash plugins

## Heartbeat

- Check if elasticsearch is up and running correctly
- Periodic messages to ES or any other destination
- The message is sent to a index called `heartbeat`
- If `epoch` is specified, it will emit the time event under a field called `clock`
- If `sequence` is specified, a sequence number of the heartbeat is added to field `clock`

## Generator

- Generate random data

## Dead letter queue

- When ES cannot process a given document, the document is rejected
  - E.g., pass a boolean value to a int field
- With Dead letter queue activated, the dead letters are store in the `dead letter path` so that they are not lost

1. Modify `/usr/share/logstash/config/logstash.yml`
1. Insert line `dead_letter_queue_enable: true`
1. Insert line `path.dead_letter_queue: /home/student/dlq`
1. check the status of the queue <http://localhost:9600/_node/stats/pipelines>

## HTTP Poller

- Poll http endpoints periodically and store the response in ES

## Twitter

- Stream twitter events directly to ES

# OTLP (OpenTelemetry Protocol)

- It's the wire format that OpenTelemetry-instrumented apps use to send traces, metrics, and logs to a backend (collector, processor, or vendor like Honeycomb / Datadog / Jaeger).

Two transports, conventional ports:

4317 — gRPC (binary, more efficient, the default)
4318 — HTTP/1.1 with protobuf or JSON body (easier to debug, works through proxies that don't speak gRPC)
Payloads are protobuf-encoded OTLP*Request messages (ExportTraceServiceRequest, ExportMetricsServiceRequest, ExportLogsServiceRequest).

Mental model: OTLP is to OpenTelemetry what statsd is to metrics or syslog is to logs — a vendor-neutral wire protocol so instrumented apps don't have to know what backend they're shipping to.

Standard reference: <https://opentelemetry.io/docs/specs/otlp/>

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-processor
  labels:
    app: my-processor
spec:
  type: ClusterIP
  selector:
    app: my-processor
  ports:
    - port: 4317
      targetPort: 4317
      protocol: TCP
      name: otlp-grpc
    - port: 4318
      targetPort: 4318
      protocol: TCP
      name: otlp-http
```

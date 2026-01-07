# WorkflowTemplate

```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: http-base
spec:
  arguments:
    parameters:
      - name: endpoint
        description: Endpoint where should to be send the request
      - name: method
        description: Http method used in the request
      - name: payload
        description: Body of the request to send

  podMetadata:
    annotations:
      iam.amazonaws.com/role: arn:aws:iam::123456789012:my-role

  templates:
    - name: my-request
      inputs:
        parameters:
          - name: endpoint
          - name: method
          - name: payload
      container:
        image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/mirror/curlimages/curl:latest
        command:
          - sh
          - -c
          - |-
            HTTP_CODE=$(curl -vv -s \
              -H "Authorization:Bearer $(cat /data/access_token)"  \
              -H "Content-type: application/json" \
              -H "Accept: application/json; charset=utf-8" \
              --data '{{inputs.parameters.payload}}' \
              --key /data/key.pem \
              --cert /data/cert.pem \
              -X {{inputs.parameters.method}} "{{inputs.parameters.endpoint}}" \
              -o /dev/stderr \
              -w "%{http_code}")
            if [ "$HTTP_CODE" -lt 200 ] || [ "$HTTP_CODE" -gt 299 ]; then
              echo "ERRO: A requisição falhou com status $HTTP_CODE"
              exit 1
            fi
        volumeMounts:
          - mountPath: /data
            name: data
      initContainers:
        - name: secrets-server
          command:
            - /bin/sh
            - -c
          args:
            - |-
              exec java ...
          env:
            - name: OTEL_METRICS_EXPORTER
              value: none
            - name: OTEL_LOGS_EXPORTER
              value: none
            - name: OTEL_TRACES_EXPORTER
              value: none
          image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-image
          imagePullPolicy: Always
          resources:
            limits:
              cpu: "1"
              memory: 1Gi
            requests:
              cpu: "1"
              memory: 1Gi
          volumeMounts:
            - mountPath: /data
              name: data
      volumes:
        - emptyDir: {}
          name: data
```

## Using a Template

```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: evidence-template
spec:
  arguments:
    parameters:
      - name: dashboard-id
        description: Grafana dashboard ID (numeric or UID)
      - name: variables
        description: 'JSON object with dashboard variables. Ex. {"DATASOURCE": "staging-metrics"}'
      - name: from
        description: Start datetime in ISO 8601 (UTC). Ex. 2025-12-17T18:00:00.000Z
      - name: to
        description: End datetime in ISO 8601 (UTC), after "from". Ex. 2025-12-17T20:00:00.000Z

  templates:
    - name: collect-evidences
      inputs:
        parameters:
          - name: dashboard-id
            description: Grafana dashboard ID (numeric or UID)
          - name: variables
            description: 'JSON object with dashboard variables. Ex. {"DATASOURCE": "staging-metrics-ist"}'
          - name: from
            description: Start datetime in ISO 8601 (UTC). Ex. 2025-12-17T18:00:00.000Z
          - name: to
            description: End datetime in ISO 8601 (UTC), after "from". Ex. 2025-12-17T20:00:00.000Z
      steps:
        - - name: run-request
            templateRef:
              name: http-base
              template: my-request
            arguments:
              parameters:
                - name: endpoint
                  value: "https://mygrafana.com"
                - name: method
                  value: "POST"
                - name: payload
                  value: |
                    {
                      "evidence-type": "grafana",
                      "from": "{{inputs.parameters.from}}",
                      "to": "{{inputs.parameters.to}}",
                      "dashboard-id": "{{inputs.parameters.dashboard-id}}",
                      "variables": {{inputs.parameters.variables}}
                    }
```

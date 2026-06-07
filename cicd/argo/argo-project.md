# Argo Project

- `Argo Events`: ingest events from sources (webhooks, s3, sqs, etc) and trigger actions. Usually the kickoff to the Workflows
- `Argo Workflows`: CI part - build, test, package, etc
- `Argo CD`: CD part, compare desired (in git) and actual state (in cluster) and reconciles drifts
- `Argo Rollouts`: progressive delivery. Provide canary and blue-green deployments

## Flow

Git push
  → Argo Events (webhook EventSource + Sensor)
    → Argo Workflows (build, test, scan, push image) - create a tag with the same git commit SHA (or the image digest - crypto hash SHA-256)
      → commit to config repo (the GitOps repo)
        → Argo CD (detects Git change, syncs to cluster)
          → Argo Rollouts (canary/blue-green with metric analysis/analysisrun with successCondition and failureCondition)

`Events` = trigger
`Workflows` = CI (build/test)
`Argo CD` = CD via GitOps (deploy)
`Rollouts` = progressive delivery (safe release)

A key distinction worth remembering: Argo Workflows uses a push model for running jobs, while Argo CD uses a pull/reconcile GitOps model for deployments — they're complementary, not competing.

## Details

- Are the projects under the Argo umbrella stateful? What state does it persist and how? Is there another project backing this state management? E.g., a workflow processing queue
  - **Answer**: Argo Workflows is mostly stateless, it's stateful part is managed by Kubernetes itself, which is scheduling jobs and the kube-scheduler. Optionally you can have a PG db for auditing completed jobs

- How to inject secrets into Workflows?
  - **Answer**: Bind the `ServiceAccount to an IAM identity` (Pod identity) or `ESO` (External Secret Operator)

- How to watch logs and metrics from Workflows? And how to display it on the PR pipeline on Github?
  - **Answer** Logs are ephemeral and can be accessed from the pods, but these pods are also garbage-collected from etcd. Every step pod has the label `workflows.argoproj.io/workflow=<name>`. You can also report status back to the commit SHA via Github API

- How does argo handle multi-region rollouts? Does it replicate the docker images from the registries in different regions?
  - **Answer**: its the artifact's registry the responsibility of replicating the image across regions. To ensure the image is replicated you can impose this condition before committing the digest bump. Or set this condition on the Rollout itself

- How to isolate the pipelines, enforce fairness, and prevent noisy neighbor issues? (one team slowing down all the platform)
  - **Answer**: Kubernetes native `namespaces` + `ResourceQuota`. Or dedicated node pools per team/tier, along with Karpenter NodePool per team, so a team's spike scales its own pool. Also `Argo concurrency controls`: max concurrent workflows per namespace/tier.

- How to self-remediate: If pipeline is too slow how to be alerted and fix it
  - **Answer**: Use `Karpenter` (cluster autoscaling) so spikes get capacity within teams budget.

- How to observe the platform: workflow count, queue depth, pod pending time, CPU/mem usage, cost/showback. Detect the noisy team, alert, and feed self-remediation. Showback, chargeback
  - **Answer**: Grafana Dashboards + Alertmanager - What to monitor?, Workflow count, Workflow latency, Workflow failure ratio, Workflows pending/processing (queue size), Total CPU usage, Costs per team/tier (enforce team label with Kyverno)

- How to enforce security gates and non-bypassable guardrails to ensure compliance and prevent engineers to bypass quality checks?
  - **Answer**: branch protection. Example: only `code owners can push` to a branch, and pushed to master branch only through PRs that need to be approved by other team members.
  - Require `mandatory status checks` to pass before merging. `Signed commits`.
  - Centralized, platform-owned pipeline templates (`ClusterWorkflowTemplate`), engineers can't edit the template
  - OPA Gatekeeper: enforce conditions on the Admission control (ValidatingAdmissionPolicy) - image signature, immutable digest, scan clean, k8s labels. The admission runs in the cluster
  - GitOps as the only path! No manually kubectl apply

- How to handle HOT fixes?
  - **Answer**: hotfix is a fast lane, not a bypass. Rollback before rollfoward.
    - Run an expedited pipeline with dedicated node pools, skip non-blocking steps

- Failed deployment, automatic rollback, canary deployments?
  - **Answer**: handled by Argo Rollouts

- How to survive production chaos, don't focus only on the success/path path. How retries are handled?
  - **Answer**: each step in the pipeline is decoupled with it's own pod, if any step fails, it won't need to restart the whole Workflow, just continue from where it left-off.
  - Argo retryStrategy with exponential backoff + jitter: no retry storm
  - For the Rollout it assumes it's bad until SLOs prove otherwise

- How to ensure an image is built only once and push once to the artifact registry?
  - **Answer** it's only one image digest for all environments/regions. Push-once. Also it's immutable tags and check before build.

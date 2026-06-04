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

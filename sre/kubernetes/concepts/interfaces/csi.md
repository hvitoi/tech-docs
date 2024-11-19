# Container Storage Interface (CSI)

- CNI allows multiple storage solutions be compatible with Kubernetes
- Allows any container orchestration tool to work with any storage vendor with supported plugin
- It defines a set of RPCs called by the container orchestrator and must be implemented by the storage drivers

- `CreateVolume`: Call (provision new volume) -> Should (provision new volume on the storage)
- `DeleteVolume`: Call (delete volume) -> Should (decommission a volume)
- `ControllerPublishVolume`: Call (place workload that uses volume onto a node) -> Should (make volume available on a node)

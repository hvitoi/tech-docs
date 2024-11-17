# cloud-controller-manager

- Embeds cloud-specific control logic
- It only runs controllers that are specific to your cloud provider (on-premise clusters will not have this component)

## Node Controller

- Checks with the cloud provider to determine if a node has been deleted in the cloud after it stops responding

## Route Controller

- Sets up routes in the underlying cloud infrastructure

## Service Controller

- Creates, updates and deletes cloud provider load balancers

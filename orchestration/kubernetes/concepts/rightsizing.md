# Rightsizing

- Use tools to rightsize requests
  - Kubecost
  - Stormforge
  - Goldilocks
  - Cloudwatch Container Insights

- This helps tuning the right resources configuration (requests and limits)
- These tools check the actual pod resources utilization over time and make recommendations
- Always configure `requests=limits` for non-CPU resources

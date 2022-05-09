# Data Transfer

- Example: transfer `200 TB` to AWS with `100 Mbps` internet connection

- **Over the internet / Site-to-Site VPn**
  - Immediate Setup
  - 100 Mbps -> 185 days
- **Over Direct Connect DX**
  - One month setup
  - 1 Gbps -> 18.5 days
- **Snowball**
  - 3 snowballs request
  - 1 week for the end-to-end transfer
- **On-going replication**
  - S2S VPN, DX with DMS, DataSync

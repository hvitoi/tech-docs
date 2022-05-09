# Storage Gateway

- Bridge between on-premises data and cloud data in S3
- Kinds
  - `File Storage Gateway`
  - `Volume Storage Gateway`
  - `Tape Storage Gateway`
- The gateway has to be installed in your on-premises environment
- A Storage Gateway `Hardware Appliance` can be bought as the physical infrastructure (mini server) for the gateway

![Storage Gateway](../../../images/storage-gateway.png)

## File Gateway

- Access `S3 files` with `NFS` or `SMB` protocols
- Integrated with `AD` for user authentication with the file gateway

![File Gateway](../../../images/file-gateway.png)

## Volume Gateway

- Access `EBS snapshots` (backed in s3) with `iSCSI` protocol
- Useful to backup on-premise volumes!

- `Cached volumes` (low latency)
- `Stored volumes`

![Volume Gateway](../../../images/volume-gateway.png)

## Tape Gateway

- Access `Virtual Tape Library (VTL)` (backed in S3) with `iSCSI` protocol

![Tape Gateway](../../../images/tape-gateway.png)

# High Performance Computing (HPC)

- **AWS Direct Connect**
  - Move GB of data to the cloud over a private network
- **Snowball & Snowmobile**
  - Move PB of data to the cloud
- **AWS DataSync**
  - Move large data from on-premise to S3, EFS, ESx for Windows

## Enhanced Networking (SR-IOV)

- Use `EC2 Placement Groups` to place the instances in a single rack

- **Elastic Network Adapter** (ENA)

  - Higher `bandwight`, higher `PPS` (packet per second), lower `latency`
  - Up to 100 Gbps
  - Legacy ENA: Intel 82599 VG (10 Gbps)

- **Elastic Fabric Adapter** (EFA)
  - Improved ENA
  - Linux only
  - Inter-node communication
  - Leverages `Message Passing Interface` (MPI): bypasses the underlying linux OS
  - Low l

## Storage

- `Instance-attached storage`
  - EBS, Instance Store
- `Network storage`
  - S3, EFS, FSx for Lustre

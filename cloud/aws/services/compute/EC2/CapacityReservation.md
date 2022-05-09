# AWS::EC2::CapacityReservation

- Pay to `reserve instance` types (e.g., m5.2xlarge) to always be available for you
- `Manual` or `planned` end-date for the reservation
- Capacity reservation is done per `AZ`

```yaml
Type: AWS::EC2::CapacityReservation
Properties:
  AvailabilityZone: String
  EbsOptimized: Boolean
  EndDate: String
  EndDateType: String
  EphemeralStorage: Boolean
  InstanceCount: Integer
  InstanceMatchCriteria: String
  InstancePlatform: String
  InstanceType: String
  TagSpecifications:
    - TagSpecification
  Tenancy: String
```

- **Reserved Instance**

  - 1 year or 3 years reservation
  - Offering classes:
    - `Reserved instance`
    - `Convertible Reserved Instance` (changable type)
    - `Scheduled Reserved Instance` (schedulable provisioning)
  - Payment option: `no upfront`, `partial upfront`, `all upfront` (up to 75% discount)

- **Dedicated Instance**

  - Also `dedicated physical server`
  - But the billing is still per instance
  - No access to the underlying hardware

# getcap

- Get the capabilities of a process
- Returns a hex code for each capability. decode it with `capsh --decode <hex>`

```shell
# Get the capabilities of a process
getcap /proc/<pid>/status | grep Cap
```

## Capabilities types

- `Permitted` (CapPrm)
  - Previously known as "forced"
  - What operations can be enabled/disabled
- `Inheritable` (CapInh)
  - Previously known as "allowed"
- `Effective` (CapEff)
  - What operations a process can perform

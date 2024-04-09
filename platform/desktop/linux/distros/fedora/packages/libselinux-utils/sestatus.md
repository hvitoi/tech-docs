# sestatus

- Get the SELinux states and modes
- SELinux modes
  - `Enforcing`
  - `Permissive`
  - `Disabled`

```shell
sestatus
```

- With enforcing mode, if you are getting login or permission errors, try `fixfiles onboot`

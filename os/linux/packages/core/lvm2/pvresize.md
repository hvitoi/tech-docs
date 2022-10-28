# pvresize

- Resize a physical device
- Useful when a physical partition has been enlarged/shrank
- This will automatically detect the new size of the device and extend the PV to its maximum

```sh
pvresize "/dev/sdx1"
```

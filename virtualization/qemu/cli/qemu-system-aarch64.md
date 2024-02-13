# qemu-system-aarch64

```shell
qemu-system-aarch64 \
  -accel hvf \
  -accel tcg \
  -cpu host \
  -M virt,highmem=on \
  -drive file=/opt/homebrew/share/qemu/edk2-aarch64-code.fd,if=pflash,format=raw,readonly=on \
  -drive file=/Users/me/.local/share/containers/podman/machine/qemu/podman-machine-default_ovmf_vars.fd,if=pflash,format=raw \
  -m 2048 \
  -smp 5 \
  -fw_cfg name=opt/com.coreos/config,file=/Users/me/.config/containers/podman/machine/qemu/podman-machine-default.ign \
  -qmp unix:/var/folders/gz/4t9dkw6n7y389ybz09jl1xdw0000gn/T/podman/qmp_podman-machine-default.sock,server=on,wait=off \
  -netdev socket,id=vlan,fd=3 \
  -device virtio-net-pci,netdev=vlan,mac=5a:94:ef:e4:0c:ee \
  -device virtio-serial \
  -chardev socket,path=/var/folders/gz/4t9dkw6n7y389ybz09jl1xdw0000gn/T/podman/podman-machine-default_ready.sock,server=on,wait=off,id=apodman-machine-default_ready -device virtserialport,chardev=apodman-machine-default_ready,name=org.fedoraproject.port.0 \
  -pidfile /var/folders/gz/4t9dkw6n7y389ybz09jl1xdw0000gn/T/podman/podman-machine-default_vm.pid \
  -device qemu-xhci \
  -device usb-host,vendorid=1921,productid=21904 \
  -virtfs local,path=/Users,mount_tag=vol0,security_model=none \
  -virtfs local,path=/private,mount_tag=vol1,security_model=none \
  -virtfs local,path=/var/folders,mount_tag=vol2,security_model=none \
  -drive if=virtio,file=/Users/me/.local/share/containers/podman/machine/qemu/podman-machine-default_fedora-coreos-39.20240128.2.2-qemu.aarch64.qcow2
```

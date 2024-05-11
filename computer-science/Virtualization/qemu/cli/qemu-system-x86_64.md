# qemu-system-x86_64

- Emulate (or virtualize) x86_64 architecture

```shell
qemu-system-x86_64 \
  -enable-kvm \
  -cdrom "Manjaro.iso" \
  -boot "menu=on" \
  -drive file=MyImage.img \
  -m 2G \
  -cpu host \
  -smp 2 \ # cores
  -vga qxl \
  -display sdl,gl=on
```

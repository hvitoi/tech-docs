# make

- Utility to manage programs
- It's a `universal packager` for linux distributions
- In archlinux it's more common to use `PKGBUILD`

```makefile
BINDIR := /usr/bin
SYSDIR := /etc/systemd/system

all:

install:
  mkdir -p ${DESTDIR}${BINDIR}
  cp sway_setup.sh ${DESTDIR}${BINDIR}
  chmod +x ${DESTDIR}${BINDIR}/sway_setup.sh
  mkdir -p ${DESTDIR}${SYSDIR}
  cp sway-start.service ${DESTDIR}${SYSDIR}
  mkdir -p ${DESTDIR}/usr/share/sway-eGPU-setup

uninstall:
  systemctl disable sway-start.service
  rm -f ${DESTDIR}${BINDIR}/sway_setup.sh
  rm -f ${DESTDIR}${SYSDIR}/sway-start.service
  rm -rf ${DESTDIR}/usr/share/sway-eGPU-setup
  rm -f /etc/environment.d/10sway.conf
```

```shell
make "install"
make "uninstall"
```

# Variables
BINDIR := /usr/bin
SYSDIR := /etc/systemd/system

VAR := value              # Simple expansion (evaluated once)
VAR = value              # Recursive expansion (evaluated each use)
VAR ?= value             # Set only if not already set

CONTAINER_RUNTIME := $(shell \
  if command -v docker >/dev/null 2>&1; then \
      echo "docker"; \
  elif command -v podman >/dev/null 2>&1; then \
      echo "podman"; \
  fi)

# Conditionals
ifeq ($(BINDIR),none) # if $BINDIR == none
    $(error No bindir found) # raise an error on makefile
endif

# Target
all:
	g++ main.cpp
  echo $(VAR) # Reference variable
  echo $(shell ls -la) # Run shell command and capture output

# Target
install:
  mkdir -p ${DESTDIR}${BINDIR}
  cp sway_setup.sh ${DESTDIR}${BINDIR}
  chmod +x ${DESTDIR}${BINDIR}/sway_setup.sh
  mkdir -p ${DESTDIR}${SYSDIR}
  cp sway-start.service ${DESTDIR}${SYSDIR}
  mkdir -p ${DESTDIR}/usr/share/sway-eGPU-setup

# Target
uninstall:
  systemctl disable sway-start.service
  rm -f ${DESTDIR}${BINDIR}/sway_setup.sh
  rm -f ${DESTDIR}${SYSDIR}/sway-start.service
  rm -rf ${DESTDIR}/usr/share/sway-eGPU-setup
  rm -f /etc/environment.d/10sway.conf

# Target + Dependencies (prerequisites)
setup-local: all install # the command below will run only after the prerequisites are complete
  @echo foo # execute a bash command (@ or TAB)
  @if docker ps -q | grep -q .; then
        echo "Running";
    fi

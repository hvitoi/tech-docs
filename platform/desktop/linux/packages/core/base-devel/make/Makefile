# Variables
BINDIR := /usr/bin
SYSDIR := /etc/systemd/system

MYVAR := anything!              # Simple expansion (evaluated once)
MYVAR = anything!              # Recursive expansion (evaluated each use)
MYVAR ?= anything!             # Set only if not already set

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
		# ... do something else

# Not equal
ifneq "${DEBUG}" "1"
	DEBUG=0
endif


# Target + Dependencies (prerequisites)
all: install uninstall # the command below will run only after the prerequisites are complete
	echo $(MYVAR) # By default, make prints each recipe line before executing it
	@echo $(MYVAR) # with @ the command won't be printed. You can also omit it with "make -s"

# Target
install:
	echo "I'm installing..."
	echo "Argument provided: $(my_arg)" # make install my_arg=hii

# Target
uninstall:
	echo "I'm uninstalling..."

# Target (with build-in make functions, Make evaluates them itself, before any recipe runs)
# Function are written $(name args)
awesome:
	if docker ps -q | grep -q .; then \
		echo "Running"; \
	fi

	# if: inline condition (alternative to the bash if)
	$(if 1, echo "a", echo "b")

	# shell
	echo $(shell ls) # Run shell command and capture output

	# wildcard: outputs the list of files that matches the glob pattern (if nothing matches, returns an empty string)
  ifeq ($(wildcard *.go),) # returns an empty string
		echo "No go files in this folder"
  endif

	# call: call a variable as if it were a function
	$(call do_something,$(MYVAR))

define do_something
	echo "Printing variable value: $(1)"
endef

# Special built-in targets

# Those targets will not print the command to be executed (even those without the preceding @)
.SILENT: install awesome # omit the target to silence all the targets
.PHONY: # mark that a target is a name for actions, not files




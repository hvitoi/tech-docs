# "if" statement with any command
foo=htop
if command -v $foo; then
  echo "Command available"
else
  echo "Command not available"
fi

# Input to if as output of a command
for boot_vga in /sys/bus/pci/devices/*/boot_vga; do
  if [ $(<"${boot_vga}") -eq 0 ]; then
    echo "It's the boot vga"
  fi
done

# "if" with [] (uses the "test" command)
# POSIX!

foo=10
if [ $foo -eq 10 ]; then # same as "if test $foo -eq 10; then"
  echo "Is equal"
else
  echo "Is not equal"
fi

# Or condition
if [ "$res" -ne 0 ] || [ -z "$macos_ver" ]; then
  exit 1
fi

# "if" with [[]]
# NON-POSIX! Bash extension

if [[ 10 > 9 ]]; then
  echo "Is greater"
else
  echo "Is not greater"
fi

folders=("document" "image" "music")
if [[ ! " ${folders[*]} " =~ " $1 " ]]; then
  echo >&2 "Folder not allowed."
  return 1
fi

if [[ $EXCEPTION_MSG == "foo"* ]]; then
  echo "it starts with foo"
fi

## inline
if [ ! -z "$foo" ]; then echo "foo"; else echo "bar"; fi

## elif

num=9
if [ $num -gt 0 ]; then
  echo "Positive!"
elif [ $num -lt 0 ]; then
  echo "Negative!"
else
  echo "Zero!"
fi

# Iterates over a list

# Literal
for el in "a" "b" "c"; do
  echo "$el"
done

# Array
items=("a" "b" "c")
for el in "${items[@]}"; do
  echo "$el"
done
foo=("a" "b" "c")
for ((i = 0; i < ${#foo[@]}; i++)); do
  echo $i
  echo ${foo[$index]}
done

# Command
for el in $(seq 1 5); do
  echo "$el"
done

# prefer using while with read!
for word in $(cat ~/.zshrc); do
  echo $word
done

# Sequence
for el in {1..5}; do # same as 1 2 3 4 5
  echo "$el"
done

# Globbing
for file in ~/.config/*; do
  echo "$file"
done

boot-vga() {
  for boot_vga in /sys/bus/pci/devices/*/boot_vga; do
    vga_device=$(dirname -- "${boot_vga}")
    for dev in "${vga_device::-1}"*; do
      echo "Device: ${dev}. Boot?: $(<"${boot_vga}")"
    done
  done
}

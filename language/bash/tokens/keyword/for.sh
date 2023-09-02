# Iterates over a list

for i in $(seq 1 5); do
  echo $i
done

for i in 1 2 3 4 5; do
  echo "Welcome $i times"
done

for letter in 'a' 'b' 'c'; do
  echo $letter
done

for i in eat run jump play; do
  echo $i
done

for i in {1..5}; do # same as 1 2 3 4 5
  touch $i
done

for file in ~/.config/*; do
  echo $file
done

for word in $(cat ~/.zshrc); do
  echo $word
done

boot-vga() {
  for boot_vga in /sys/bus/pci/devices/*/boot_vga; do
    vga_device=$(dirname -- "${boot_vga}")
    for dev in "${vga_device::-1}"*; do
      echo "Device: ${dev}. Boot?: $(<"${boot_vga}")"
    done
  done
}

foo=("a" "b" "c")
for ((i = 0; i < ${#foo[@]}; i++)); do
  echo $i
  echo ${foo[$index]}
done

my_function() {
  echo "lol"
}

my_function # execute

##

$(pwd)

##

f() {
  folders=("document" "image" "music")
  if [[ ! " ${folders[*]} " =~ " $1 " ]]; then
    echo >&2 "Folder not allowed."
    return 1
  fi
  echo $1
  unset -f f
}
f

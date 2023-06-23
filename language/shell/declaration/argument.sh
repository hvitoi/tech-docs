echo "Zero arg (the fucntion itself): $0"
echo "First arg: $1"
echo "First arg: ${1-falback}" # uses fallback if $1 is empty
echo "Second arg: $2"
echo "All args: $@" #  in an array
echo "All args: $*" #  in string separated by spaces
echo "Number of args: $#"

arguments() {
  echo The function location is $0
  echo There are $# arguments
  echo "Argument 1 is $1"
  echo "Argument 2 is $2"
  echo "<$@>" and "<$*>" are the same.
  echo List the elements in a for loop to see the difference!
  echo "* gives:"
  for arg in "$*"; do echo "<$arg>"; done
  echo "@ gives:"
  for arg in "$@"; do echo "<$arg>"; done
}

arguments hello world

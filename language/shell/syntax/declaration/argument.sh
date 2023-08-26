echo "Zero arg (the fucntion itself): $0"
echo "First arg: $1"

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

# Fallback
echo "First arg: ${1-Undefined}" # uses "Undefined" if $1 is empty
echo "The arg: ${1:-Undefined}"  # uses "Undefined" if $1 is empty

# Parameter expansion: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02
where ${var+Other}

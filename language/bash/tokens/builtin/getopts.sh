# - `$OPTARG`: the current argument value
# - `$OPTIND`: the position of the current argument

while getopts hl: arg; do
  case "${arg}" in
  l)
    launcher=$OPTARG
    echo "$launcher"
    ;;
  h)
    usage
    exit 0
    ;;
  *)
    usage
    exit 1
    ;;
  esac
done

shift $((OPTIND - 1))

echo "$@"

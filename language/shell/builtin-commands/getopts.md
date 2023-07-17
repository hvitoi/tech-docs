# getopts

- `$OPTARG`: the current argument value
- `$OPTIND`: the position of the current argument

```shell
while getopts hl: arg; do
  case "${arg}" in
  l) launcher=$OPTARG ;;
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

echo $@
```

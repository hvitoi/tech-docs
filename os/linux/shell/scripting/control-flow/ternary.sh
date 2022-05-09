# Ternary
case "$b" in
5) a=$c ;;
*) a=$d ;;
esac

# Ternary shorter
[[ $b = 5 ]] && a="$c" || a="$d"

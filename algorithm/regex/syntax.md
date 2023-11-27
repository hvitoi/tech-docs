# Syntax

```shell
set data '
     a
!
a
A
foo
999
barr
ba
bar9
a-b-c-d
Bar
foofoo
foolalabar
foo.txt
bar.txt
foo1.txt
bar1.doc
foobar.txt
foo.doc
bar.doc
dataset.txt
purchase.db
purchase1.db
purchase2.db
purchase3.db
purchase.idx
foo2.txt
bar.txt'
```

## `^` `$` (Anchors)

- Force match to `start` (^) or `end` ($) of a line

```shell
# starting with pur
echo $data | grep -E '^pur'

# ending with db
echo $data | grep -E 'db$'

# single char only
echo $data | grep -E '^.$'

# exact match
echo $data | grep -E '^foo$'
echo $data | grep -E '^$' # blank only
```

## `()`

```shell
echo $data | grep -E 'foo(foo|bar)' # foofoo or foobar
```

## `[]` (Sets)

- Matching Sets of Characters contained in the square brackets

```shell
# set of characters
echo $data | grep -E '[Bb]ar'
echo $data | grep -E '[Bb][Aa][Rr]' # Bar, bAr, BAr, baR, etc

# range of characters (range is specified from ascii table codes)
echo $data | grep -E 'bar[0-9]'
echo $data | grep -E '[0-9]' # at least one number
echo $data | grep -E '[A-z]' # at least one letter (case insensitive)
echo $data | grep -E '[A-z0-9]' # At least one number or one letter (case insensitive)

# range negation
echo $data | grep -E 'bar[^0-9]' # next char is not a digit
echo $data | grep -E 'bar[^[:digit:]]' # same

# bracket expressions (not universal)
echo $data | grep -E '[[:alnum:]]' # At least one Alphanumeric character
echo $data | grep -E '[[:alpha:]]' # .. Alphabetic character
echo $data | grep -E '[[:blank:]]' # .. Blank character (space and tab)
echo $data | grep -E '[[:digit:]]' # .. Digit (0 1 2 3 4 5 6 7 8 9)
echo $data | grep -E '[[:lower:]]' # .. Lower-case letter (a b c d e f g h i j k l m n o p q r s t u v w x y z)
echo $data | grep -E '[[:space:]]' # .. Space character (tab, newline, vertical tab, form feed, carriage return, and space)
echo $data | grep -E '[[:upper:]]' # .. Upper-case letter (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)
```

## `|` (or)

```shell
# contains letters or digits
echo $data | grep -E 'foo|bar'
echo $data | grep -E '[A-z]|[0-9]'
```

## `.` (Single match)

- Matches a single character (any)

```shell
# anything (even empty)
echo $data | grep -E ''

# has at least one char
echo $data | grep -E '.'

# has f following by at least one char
echo $data | grep -E 'f.'

# Match purchaseX followed by at least a char and a dot after
echo $data | grep -E 'purchase.\.'

# at least two characters
echo $data | grep -E '..'

# has purchase followed by any 2 chars
echo $data | grep -E 'purchase..'

# has purchase, followed by any single character in between, followed by db
echo $data | grep -E 'purchase.db'
```

## `?` (optional pattern)

```shell
# The preceding item is optional and will be matched, at most, once.
echo $data | grep -E 'bar?' # bar, ba
```

## `*` (optional or multiple pattern)

```shell
# The preceding item will be matched zero or more times
echo $data | grep -E 'bar*' # ba, bar, barr
```

## `+` (multiple pattern)

```shell
# The preceding item will be matched one or more times.
echo $data | grep -E 'bar+' # bar, barr
```

## `{}` (number of occurrences)

```shell
# 1 to 3 letters
echo $data | grep -E '[A-z]{1,3}'

# at least 3 letters
echo $data | grep -E '[A-z]{3,}'

# exactly 3 letters
echo $data | grep -E '[A-z]{3}'

# ip address mask
echo $data | grep -E '[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}'

# telephone number (91-1234567890)
echo $data | grep -E '[[:digit:]]\{2\}[ -]\?[[:digit:]]\{10\}'
```

## `\<` `\>` (empty strings at start or end)

```shell
# start with empty strings (or not), followed by "a"
echo $data | grep -E '\<a'

# end with empty strings (or not), preceded by "a"
echo $data | grep -E 'a\>'
```

## `\d` (digits)

```shell
# At least one digit
echo $data | grep -E '\d'
```

## `\D` (non-digits)

```shell
# At least one non-digit
echo $data | grep -E '\D'
```

## `\w` (whole word)

```shell
# At least one whole word
echo $data | grep -E '\w'
```

## `\W` (non whole word)

```shell
# At least one non whole word
echo $data | grep -E '\W'
```

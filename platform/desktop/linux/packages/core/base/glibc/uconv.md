# iconv

- Convert text encodings
- Supports some advanced Unicode stuff

```shell
# Displays hex codes or actual names of characters (useful for debugging)
uconv -f utf-8 -t utf-8 -x '::Any-Hex;' < input.txt
uconv -f utf-8 -t utf-8 -x '::Any-Name;' < input.txt

# Lowercase and removes all accents (by expanding and dropping them)
uconv -f utf-8 -t utf-8 -x '::Any-Lower; ::Any-NFD; [:Nonspacing Mark:] >; ::Any-NFC;' < input.txt > output.txt
```

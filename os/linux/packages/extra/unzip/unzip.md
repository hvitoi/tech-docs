# unzip

```shell
unzip "file.zip"
unzip "file.zip" -d "dest-folder"
```

```shell
# unzip multi-part zip
cat "parts-*" > "full-broken.zip"
zip -FF "full-broken.zip" --out "full-fixed.zip"
unzip "full-fixed.zip"
```

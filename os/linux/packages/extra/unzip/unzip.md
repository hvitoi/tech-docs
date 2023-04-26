# unzip

```shell
unzip "file.zip"
unzip "*.zip" # extract all zips in a folder
```

```shell
# unzip multi-part zip
cat "parts-*" > "full-broken.zip"
zip -FF "full-broken.zip" --out "full-fixed.zip"
unzip "full-fixed.zip"
```

## -d

- Extract into a directory

```shell
# extract into a exdir
unzip "file.zip" -d "dest-folder"
unzip 'multipartfile.zip*' -d combined
```

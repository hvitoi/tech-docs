# sed

- Replace string with a newstring
- Find and delete line
- Remove empty lines
- Replace tabs with spaces

```sh
# s - substitute
# g - global (entire file)
sed 's/word/newword/g' "file.txt" # Substitute but does not save
sed 's/word//g' "file.txt" # Substitute with nothing
sed 's/\t/ /g' "file.txt" # substitute tab "/t" with spaces " "
sed -i 's/word/newword/g' "file.txt" # Substitute and save

# d - delete
sed '/word/d' "file.txt" # Delete the line with the word
sed '/^$/d' "file.txt" # Delete empty lines. ^ anything that starts. $ anything that ends. In the middle there is nothing, so empty line
sed '1d' "file.txt" # Delete line 1
sed '1,2d' "file.txt" # Delete lines 1 and 2

# View lines
sed -n 12,18p "file.txt" # view lines 12 to 18 # 'p' for pick
sed -n 2p "file.txt" # view line 2
sed 12,18d "file.txt" # view lines but 12 to 18 # 'd' for delete

# Add empty between lines
sed G "file.txt"

# Substitute only certain occurrence
sed '8!s/word/S' "file.txt" # SUbstitute all but the line 8
```

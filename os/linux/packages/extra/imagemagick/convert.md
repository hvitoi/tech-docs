# convert

- Convert images into pdf

```shell
convert "a.png" "b.png" "out.pdf"

# Invert colors
convert -density 150 -channel RGB -negate "source-file.pdf" "output-file.pdf"

# Convert to .ico
convert logo.png -define icon:auto-resize=64,64,48,32,16 icon.ico

# Reduce size
convert -resize 170x170 -quality 72 full.png reduced.png
```

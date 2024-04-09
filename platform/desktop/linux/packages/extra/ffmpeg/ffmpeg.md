# ffmpeg

- Generate video thumbnails

```shell

ffmpeg \
  -framerate "25" \
  -pattern_type "glob"
  -i '*.png' \
  # -i image-%05d.png \ # takes images named e.g., image-00001.jpg, image-00002.jpg, etc
  -c:v "libx264" \ # video codec
  -profile:v "high" \ # high profile (better quality)
  -crf "20" \ # constant quality mode, very high quality
  -pix_fmt "yuv420p" \ # use YUV pixel format
  output.mp4
```

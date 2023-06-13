# notify-send

## hint

- Syntax: `TYPE:NAME:VALUE`
- Types
  - boolean
  - int
  - double
  - string
  - byte
  - variant

```shell
notify-send "Brightness" \
  --hint string:x-dunst-stack-tag:brightness \
  --hint int:value:40 \
```

## urgency

- Urgency
  - low
  - normal
  - critical

```shell
notify-send \
  --urgency normal \
  "Brightness"
```

## icon

- Icon filename or stock icon

```shell
notify-send \
  --icon "display-brightness-high-symbolic" \
  "Brightness"
```

## expire-time

```shell
notify-send \
  --expire-time 1600 \
  "Brightness"
```

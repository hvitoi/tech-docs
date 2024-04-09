# socat

```shell
#!/bin/sh
function handle() {

  event=$(echo -n $1 | awk -F '>>' '{print $1}')
  data=$(echo -n $1 | awk -F '>>' '{print $2}')

  echo $event
  echo $data

  if [ "$event" = 'activewindowv2' ]; then
    hyprctl dispatch moveworkspacetomonitor "1 1"
  fi
}

socat - UNIX-CONNECT:/tmp/hypr/$(echo $HYPRLAND_INSTANCE_SIGNATURE)/.socket2.sock | while read line; do handle $line; done
```

# pactl

- Pulse Audio CTL

## list

```shell
# List connections
pactl list
pactl list | grep -C2 A2DP

# List specific
pactl list cards
pactl list sources
pactl list sinks
pactl list modules
```

## get-default-sink

```shell
pactl get-default-sink
```

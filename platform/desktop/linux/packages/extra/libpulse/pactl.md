# pactl

- Pulse Audio CTL

## list

```shell
# List connections
pactl list
pactl -f "json" list
pactl list | grep -C2 A2DP

# List specific
pactl list cards
pactl list sources
pactl list sinks
pactl list modules
```

```shell
audio_sinks=$(
  pactl -f json list |
    jq '.sinks |
        .[] |
        {
          node_id: .index,
          node_name: .name,
          node_description: .description,
          node_nick: .properties."node.nick",
          device_id: .properties."device.id",
          device_name: .properties."device.name",
          device_nick: .properties."device.nick",
          device_port_id: .properties."card.profile.device"
        }'
)

audio_devices=$(
  pactl -f json list |
    jq '.cards |
        .[] |
        {
          device_id: .index,
          device_name: .name,
          ports: .ports
                 | to_entries
                 | map(.value)
                 | map({
                          id: .properties."card.profile.port",
                          type: .type,
                          product_name: .properties."device.product.name"
                        })

        }'
)
```

## get-default-sink

```shell
pactl get-default-sink
```

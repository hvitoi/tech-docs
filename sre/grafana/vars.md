# vars

## $__timeRange

- Time range picked from the dropdown menu

```txt
$__timeRange()
```

## $__interval

- Calculated automatically based on the `Time range` / `Max data points`
- On a 24h period and a maximized window the interval is around `1m`

```txt
$__interval
```

## $__timeGroup

- Over time graph
- Groups results in chunks of a given interval

```txt
$__timeGroup(timestamp, '1m')
```

## $MY_VAR

- Constant variable defined in the project's settings

## json_value

```txt
json_value(log, 'lax $.data.path')
```

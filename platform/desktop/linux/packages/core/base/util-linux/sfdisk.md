# sfdisk

- Scripting version of fdisk

## --list

- List partition

```shell
sfdisk /dev/diskN -l
```

## --list-free

- List free (unallocated space)

```shell
sfdisk /dev/diskN -F
```

## --move-data

- Use the output of `--list-free` empty sectors to know how many sectors to shift left/right

```shell
# Move the 1st partition by NUM sectors to the right
echo '+NUM' | sfdisk --move-data /dev/diskN -N 1

# Move the 2nd partition by NUM sectors to the left
echo '-NUM' | sfdisk --move-data /dev/diskN -N 2
```

## resize

```shell
echo ", +" | sfdisk -N 1 /dev/diskN
```

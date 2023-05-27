colors = ["blue", "green", "red"]

# the enumerated object is an iterable object with [[index1,value1], [index2,value2]] format
enumerated_colors = enumerate(colors)

for index, color in enumerated_colors:
    print(index, color)

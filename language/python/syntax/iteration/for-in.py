colors = ["blue", "green", "red"]

for color in colors:
    print(color)

for index, color in enumerate(colors):
    print(index, color)

for index in range(len(colors)):
    print(colors[index])

for index in range(10):
    print(index)

for letter in "Eu sou Henrique":
    print(letter)

# Tuples
foo = [("a", 1), ("b", 2)]
for (first, second) in foo:
    print(first)
    print(second)

with open("file.txt") as file_content:
    for line in file_content:
        print(line)

# same as:
file_content = open("file.txt")
for line in file_content:
    print(line)

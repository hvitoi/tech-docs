# readline returns an iterable over each line of the file

with open("file.txt") as f:
    for line in f:
        print(line)


open("file.txt", "r")  # read
open("file.txt", "w")  # write
open("file.txt", "a")  # append
open("file.txt", "r+")  # read and write
file = open("file.txt", "r")

print(file.readable())  # True para "r" e False para "w"
print(file.read())  # Le todas as linhas
print(file.readline())  # Le linha em ordem
empregados = file.readlines()  # grava txt em um array
file.close()

file = open("employees.txt", "a")
file.write("\nToby - Human Resources")
file.write("\nKelly - Customer Service")
file.close()

file = open("employees.txt", "w")  # overwrite the entire file
file.write("Toby - Human Resources")
file.close()

file1 = open("employees1.txt", "w")  # creates another txt file
file1.write("Toby - Human Resources")
file1.close()

#-----------------------------------
# Read Files

#open("employees.txt", "r") #read
#open("employees.txt", "w") #write
#open("employees.txt", "a") #append - add new info
#open("employees.txt", "r+") #read and write

employee_file = open("employees.txt", "r") #Grava o conteudo na variavel

print(employee_file.readable()) #True para "r" e False para "w"
#print(employee_file.read()) # Le todas as linhas
#print(employee_file.readline()) #Le linha em ordem
empregados = employee_file.readlines() #grava txt em um array
employee_file.close()

print(empregados[0])

for emp in empregados:
    print(emp)

#-----------------------------------
# Write Files

employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees.txt", "w") #overwrite the entire file
employee_file.write("Toby - Human Resources")
employee_file.close()

employee_file1 = open("employees1.txt", "w") #creates another txt file
employee_file1.write("Toby - Human Resources")
employee_file1.close()

webpage = open("index.html", "w")
webpage.write("<p>This is HTML</p>")
webpage.close()

#-----------------------------------
# Modules
import useful_module
print(useful_module.beatles)
print(useful_module.roll_dice(10))


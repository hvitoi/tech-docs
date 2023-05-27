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

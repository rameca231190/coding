# Open file inside this folder with mode read (r), write (w), append "a", read and write "r+"
employee_file = open("employees.txt", "r")

# Bellow funciton will return bulian value and it will tel use wether or not we can read the file.
#print(employee_file.readable())

# Figure out what inside file (print all content).
#print(employee_file.read())

# Read just first line of the file, if you put it 2 times it will read 2 first lines.
#print(employee_file.readline())
#print(employee_file.readline())

#Better way of reading lines.
#print(employee_file.readlines()[1])

# For loop to read the lines
for employee in employee_file.readlines():
    print(employee)


employee_file.close()
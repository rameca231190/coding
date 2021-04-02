# Append something to the file
employee_file = open("employees.txt", "a")

#\n will add an line to a new line
employee_file.write("\nToby - Human Resources")

employee_file.close()


# Write something to the file, when you use w mode it will overwrite everything inside the file
# If you create the name of the file which is not exist it will create the new file in the directory
employee_file = open("employees1.txt", "w")

#\n will add an line to a new line
employee_file.write("\nToby - Human Resources")

employee_file.close()

# Create the new HTML file

index_test = open("index.html", 'w')

index_test.write("<p>This is HTML<p>")
index_test.close()
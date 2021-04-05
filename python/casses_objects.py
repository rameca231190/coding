
# This is script is connected to Student.py
from Student import Student

student1 =  Student("Jim", "Business", 3.1, False)
student2 =  Student("Pam", "Business", 3.8, True)

print(student1.gpa)
print(student2.on_honor_roll())
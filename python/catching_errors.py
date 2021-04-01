# Try first this and if there an error except will prompt

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Devided by zero")
except ValueError:
    print("Invalid Input")
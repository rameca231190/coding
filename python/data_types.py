# Data types in python (strings, numbers)
# string (plain text)
print("Giraffe Academy")

#Print string as a new line
print("Giraffe\n Academy")

# \ Gives ability to put quotation marks to string
print("Giraffe\"Academy")

#Add one string to another.
phrase = "Giraffe Academy"
print(phrase + " is cool")

#Print as upper or lower case
print(phrase.upper())
print(phrase.lower())

#Print string with len function which wil show you amount of characters in string
print(len(phrase))

#Print character in string by position (position starting from 0)
print(phrase[0])

#Return an index from string
print(phrase.index('a'))



# numbers (when storing numbers you don't need quotation marks)
print(2.093)
print(-2.093)
print(3 * 4 + 5)
# Change the order
print(3 * (4 + 5))

# abs print negative variable it will scip negative

my_num = -5
print(abs(my_num))

print(pow(3, 2))
#max function will return the bigger number
print(max(3, 2))

#min function will return the smalest number
print(min(3, 2))

# round number is stands for okruglit :)
print(round(3.7))


# import math function

from math import *
num = 5

#floor function will grep the smalest number
print(floor(3.7))

# it will return squer root of the number
print(sqrt(36))
# Program which converts month
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}
#Method one of calling value
print(monthConversions["Feb"])

#Method two of calling value
print(monthConversions.get("Apr"))


#Call key which is not in a dictionary and assign value there thu the print
print(monthConversions.get("Luv", "Not a valid Key"))



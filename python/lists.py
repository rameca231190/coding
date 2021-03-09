#Create a list
friends = ["Kevin", "Karen", "Jim"]

#Access diferent elements in a list
print(friends[2])
print(friends[-2])
print(friends[0:3])


# More about lists
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#Extend your list with additional list
friends.extend(lucky_numbers)
# Insert another value to the list based on index position
friends.insert(1, "Kelly")
print(friends)

#Remove specific value from the list
friends.remove("Jim")
print(friends)
#Removes the last elements of the list
friends.pop()
print(friends)

#Sort the list in alphabetical order

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

#Copy one list to another

friends2 = friends.copy()
print(friends2)
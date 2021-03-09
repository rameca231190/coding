def say_hi():
    print("Hello User")


print("Top")
# Call the function
say_hi()

print("Bottom", "35")

#Give a variable to the funciton so it can use it as a name
def say_name(name, age):
    print("Hello User " + name + ", you are " + age)
    
say_name("Nastia", "30")
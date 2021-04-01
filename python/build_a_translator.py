# Translate english to the giraffe laguage

def translate(phrase):
    traslation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            traslation = traslation + "g"
        else:
            traslation = traslation + letter
    return traslation
print(translate(input("Enter a phrase: ")))
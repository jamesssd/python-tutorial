programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Retrieve items from the dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action fo doing something over and over again"

print(programming_dictionary)

#To create an empty list, you use the square brackets [], to create a dictionary, you use the curly brackets [].
#To wipe clean an excisting dictionary, you do this
#programming_dictionary = {}

#Edit an item in the dictionary
#programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
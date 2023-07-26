#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = []
# com_letter = random.choices(letters, k=nr_letters)
# password.append(com_letter)
# com_symbols = random.choices(symbols, k=nr_symbols)
# password.append(com_symbols)
# com_numbers = random.choices(numbers, k=nr_numbers)
# password.append(com_numbers)

# print(password)
#answer key for easy
# password = ""

# for char in range(1, nr_letters +1):
#     password+= random.choice(letters)

# for sym in range(1, nr_symbols + 1) :
#     password += random.choice(symbols)
    
# for num in range(1, nr_numbers +1):
#     password+= random.choice(numbers)
    
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#shuffle 

#Hard Level Answer
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")

#############
#Program Generated Password
random_num = random.randint(1,10)
random_sym = random.randint(1,5)
random_char = random.randint(1,10)
password_list = []

for char in range(1, random_char):
    password_list.append(random.choice(letters))

for sym in range(1, random_sym) :
    password_list.append(random.choice(symbols))
    
for num in range(1, random_sym):
    password_list.append(random.choice(numbers))
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list :
    password+=char
print(password)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
password = ""
for letter in range(1 ,nr_letters + 1):
    randon_number = random.randint(1,52)
    password = password + letters[randon_number]


for symbol in range(1 ,nr_symbols + 1):
    randon_number = random.randint(1,10)
    password = password + numbers[randon_number]

    
for letter in range(1 ,nr_numbers + 1):
    randon_number = random.randint(1,9)
    password = password + symbols[randon_number]
print(password)

#Hard Level

final_password = ''.join(random.sample(password,len(password)))
print(final_password)
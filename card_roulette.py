import random

print("Welcome to the card roulette!")

names_string = input("Please give me all the people's names. And seprate them by comma.")

names = names_string.split(",")

final = len(names)

lucky_number = random.randint( 0 , final - 1 ) 

print(f"Tonight {names[lucky_number]} pays for us!")
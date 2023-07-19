import random

print("Hello to heads or tails programme.")

coinflip = str(input("Do you wanna flip a coin? Y or N"))
result = random.randint(0,1)
print(result)

if coinflip == "Y":
    if result == 1 :
        print("heads")
    else:
        print("tails")
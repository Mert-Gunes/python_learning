print("Welcome To the pizza app! May I take your order?")

size = str(input("Which size do you want your pizza to be? S M or L"))

if size == "L":
    bill = 25
    pepperoni = str(input("Do you want pepperoni with your pizza? Y or N"))
    if pepperoni == "Y":
        bill = 28
if size == "M":
    bill = 20
    pepperoni = str(input("Do you want pepperoni with your pizza? Y or N"))
    if pepperoni == "Y":
        bill = 23
if size == "S":
    bill = 15
    pepperoni = str(input("Do you want pepperoni with your pizza? Y or N"))
    if pepperoni == "Y":
        bill = 17

extra_cheese = str(input("Do you want extra cheese with your pizza?"))
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill will be ${bill}")

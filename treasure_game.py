import random

print("Welcome to the treasure hunt game!")

row_1 = ["◻️","◻️","◻️"]
row_2 = ["◻️","◻️","◻️"]
row_3 = ["◻️","◻️","◻️"]
print("",row_1,"\n", row_2,"\n",row_3)

map = [row_1, row_2, row_3]

random1 = random.randint( 0 , 2)
random2 = random.randint( 0 , 2)
column = map[random1]
column[random2] = "X"


guess = str(input("Please enter a column and a row and sepreate them with comma."))

split_guess = guess.split(",")
if split_guess[0] == random1:
    if split_guess[1] ==random2:
        print("Congrats! You have found the trasure!")
    else:
        print("You haven't found the treasure")
else:
    print("You haven't found the treasure")
print("Welcome to leap year calculator.")

year = int(input("Please enter a valid year to calculate"))

year_calculated = year % 4

if year_calculated == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    else:
        print("That's a leap year!")
else:
    print("That's not a leap year.")
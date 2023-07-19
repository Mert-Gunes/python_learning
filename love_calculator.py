print("Welcome To the famous love calculator! Let us show how good you are when you are together!")

name_1 = input("Please enter first name.").lower()
name_2 = input("Please enter second name.").lower()

true_count_name_1 = name_1.count("t" & "r" & "u" & "e")
true_count_name_2 = name_2.count("t" & "r" & "u" & "e")

true_count = int(true_count_name_1) + int(true_count_name_2)

love_count_name_1 = name_1.count("l" & "o" & "v" & "e")
love_count_name_2 = name_2.count("l" & "o" & "v" & "e")

love_count = int(love_count_name_1) + int(love_count_name_2)

final_result = str(true_count) + str(love_count)

print(f"Your love score is %{final_result}")
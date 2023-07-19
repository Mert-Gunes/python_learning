print("Umarım bu sefer çalışır")


height = float(input("Please input your height by meters"))
weight = float(input("please input your weight by kilograms"))


print("Boyunuz :"+ str(height))
print("kilonuz :"+ str(weight))

bmi = weight / (height * height)
print(bmi)

if bmi > 25:
    print("You are overweight")
elif bmi < 18:
    print("You are underweight")
else:
    print("you are ok")

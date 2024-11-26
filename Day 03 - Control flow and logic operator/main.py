#checking even-odd number
#numberToCheck = int(input("Enter your number..."))

# if numberToCheck%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


#Ticket counter

# height = int(input("Enter your height\n"))
#
#
# if height >= 180:
#     age = int(input("Enter your age\n"))
#     if age <= 17:
#         print("Your ticket price is $100")
#     else:
#         print("Your ticket price is $130")
# else:
#     print("Sorry, ticket is not available for you")


##
# BMI Calculator
##
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi <= 25:
    print("overweight")


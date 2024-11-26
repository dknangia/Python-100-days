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
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("normal weight")
# elif bmi <= 25:
#     print("overweight")


###
# Python pizaa delivery
###

print('Welcome to Python Pizza delivery')
size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want Peperoni on your pizza? Y or N:")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N:")
bill = 0

if size == "s" or size == "S":
    bill = 15

elif size == "m" or size == "M":
    bill = 20
elif size == "l" or size == "L":
    bill = 25

if pepperoni == "Y" or pepperoni == "y":
    if size == "L" or size == "M":
        bill +=3
    else :
        bill += 1
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 1


print (f"Here is your total bill {bill}")



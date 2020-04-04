name = input("Please input your name: ")
age = int(input("Please input your age: "))
hasCreditCard = input("Do you have credit card? ")
if 18 <= age < 31:
    print("Welcome to the holiday, {0}".format(name))
elif age == 17 and hasCreditCard.casefold() == "yes":
    print("You are 18 this year")
else:
    print("Sorry you are not qualified for holiday")

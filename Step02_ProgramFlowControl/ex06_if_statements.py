name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("Congratulations! You are old enough to vote")
else:
    print("Please come back in {0} year(s)".format(18 - age))

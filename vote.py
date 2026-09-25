#user input
age=int(input("Enter your age: "))
#conditional statement
if age<18:
    print("You cant vote")
elif age>100:
    print("Invalid age. Enter your age again.")
else:
    print("You can vote.")



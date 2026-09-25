#Determine Wheatehr a number is even or odd

def check_even(number):
    if number%2==0:
        print("Your number is even number.")
    else:
        print("Your number is odd number.")

number=int(input("Enter Your Number: "))
check_even(number)
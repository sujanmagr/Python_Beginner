#Python Functions
'''
Syntax: def function_name():
    statement
#call/use
Function_name()
'''
#define function
#function with parameter

# def greet(name):
#     print("Welcome", name)
#     print("Namaste", name)
#     print("Hello", name)
#     print("Thankyou",name)
#     print("Goodbye", name)

# greet("Sachin")
# greet("Hari")
# greet("Ram")


#Function with Return Value

# def sum(x,y):
#     return x+y

# result=sum(4, 6)
# print(result)

# if result>10:
#     print("The sum is greator than 10")
# else:
#     print("Less than 10")
   
#FUnction with Input Values

# def sum():
#     number1=int(input("Enter your first number: "))
#     number2=int(input("Enter your second number: "))
#     print(number1)
#     print(number2)
#     result=number1+number2
#     print("The total sum is ", result)

# sum()


def greet(name="Sachin"):
    print("hello Good morning ", name)

greet("Ram")
greet()




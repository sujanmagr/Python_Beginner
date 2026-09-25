#Multiple Return Example
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
result1, result2 = calculate(20, 10)
print(result1)
print(result2)
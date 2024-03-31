# Define Functions
def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


#get user input
operation = input("Enter operation (+, -, *, /, %): ")
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))

# Operations
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = substract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else: 
    print(f"Input a valid Operation")

print(f"Answer: {result}")
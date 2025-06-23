# calculator

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y if y != 0 else "Error: Cannot divide by zero"

print("Simple Calculator")

while True:
    print("\n Select the operation:")
    print("1. Addition (+) ")
    print("2. Subtraction (-) ")
    print("3. Multiplication (*) ")
    print("4. Division (/) ")
    print("5. Exit")

    choice = input(" Enter your choice ( 1 / 2 / 3 / 4 / 5 ): ")

    if choice == '5':
        print("Exiting the calculator. Thank you!")
        break

    if choice in ( '1' , '2' , '3' , '4' ):
        try:
            num1 = float(input(" Enter first number: "))
            num2 = float(input(" Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric values. ")
            continue
        if choice == '1':
            print(f"Result : {num1} + {num2} = {add (num1 , num2)}")
            elif choice == '2':
            print(f"Result : {num1} - {num2} = {subtract (num1 , num2)}")
            elif choice == '3':
            print(f"Result : {num1} * {num2} = {multiply (num1 , num2)}")
            elif choice == '4':
            result = divide(num1 , num2 )
            print(f"Result : {num1} / {num2} = {result}")
            else:
            print("Invalid choice. Please select a valid operation.(1-5) ")










import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        x / y
        return x / y
    except ZeroDivisionError:
        print("Divide by 0 Error")

def percent(x, y):
    try:
        100 * x/y
        return 100 * x/y
    except ZeroDivisionError:
        print("Divide by 0 Error")


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Percent")
print("6.x to the power of y")
print("7.Logarithm base x of y")
print("8.Square root")
print("9.Sin")
print("10.Cos")
print("11.Tan")
print("12.Natural logarithm")



while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            num1 = float(input("Enter the first number : "))
        except ValueError:
            num1 = float(input("Please enter float number: "))

        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            num2 = float(input("Please enter float number: "))


        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} % {num2} = {percent(num1, num2)} %")

        elif choice == '6':
            print(f"{num1} pow {num2} = {pow(num1, num2)}")

        elif choice == '7':
            print(f"Logarithm base {num1} of {num2} is : { math.log(num2,num1)}")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    elif choice in ('8', '9', '10', '11', '12'):
        try:
            num1 = float(input("Enter number : "))
        except ValueError:
            num1 = float(input("Please enter float number: "))

        if choice == '8':
            print(math.sqrt(num1))

        elif choice == '9':
            print(f"sin({num1}) = {math.sin(num1)}")

        elif choice == '10':
            print(f"cos({num1}) = {math.cos(num1)}")

        elif choice == '11':
            print(f"tan({num1}) = {math.tan(num1)}")

        elif choice == '12':
            print(f"ln({num1}) = {math.log(num1)}")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

    else:
        print("Invalid Input")



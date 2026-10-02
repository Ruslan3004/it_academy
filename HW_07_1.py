# HW_07_1 Functions Exercise 1 (Calculator)

def calculator():
    print("Welcome to the calculator")

    # print("Enter a fist number")
    a = float(input("Enter the first number: "))

    # print("Enter a second number")
    b = float(input("Enter the second number: "))

    while True:

        operation = input("Enter an action (+ - * / ** %): ")
        result = 0

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b
        elif operation == "**":
            result = a ** b
        elif operation == "%":
            result = a % b
        else:
            print("Invalid operation")
            continue

        print(f"Result:  {result}")
        break


calculator()
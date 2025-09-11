while True:
    numberOne = int(input("Enter first number "))
    numberTwo = int(input("Enter second number "))
    operation = input("Choose Operation: + as addition, - as subtraction, * as multiplication, / as divide: ")

    if operation == "+":
        print("Result of addition: ", numberOne + numberTwo)
    elif operation == "-":
        print("Result of subtraction: ", numberOne - numberTwo)
    elif operation == "*":
        print("Result of multiplication: ", numberOne * numberTwo)
    elif operation == "/":
        if numberTwo == 0:
            print("Error: can't be divided by zero")
        else:
            print("Result of divide:", numberOne / numberTwo)
    else:
        print("Calculator doesn't work with another operations")

    question = input("Do you want to continue? (y/n): ").lower()
    if question not in ("y", "yes"):
        print("Calculator stopped!")
        break

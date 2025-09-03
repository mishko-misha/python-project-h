numberOne = int(input("Enter first number "))
numberTwo = int(input("Enter second number "))
operation = input("Choose Operation: + as addition, - as subtraction, * as multiplication, / as divide: ")

if operation == "+" or operation == "-" or operation == "*" or operation ==  "/":
    if  operation == "+":
        addition = numberOne + numberTwo
        print("Result of addition: ", addition)

    if operation == "-":
        subtraction = numberOne - numberTwo
        print("Result of subtraction: ",subtraction)

    if operation == "*":
        multiplication = numberOne * numberTwo
        print("Result of multiplication: ",multiplication)

    if operation == "/":
        if numberTwo == 0:
            print("Error: can't be divided by zero")
        else:
            divide = numberOne / numberTwo
            print("Result of divide:", divide)
else:
    print("Calculator doesn't work with another operations")
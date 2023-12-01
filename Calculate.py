def calculate(number1, number2, operator):
    global result
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "x":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2   
    return result
number1 = int(input("Type a number1: "))
while True:
    operator = input("Choose your operator(+,-,x,/): ")
    if operator == "+" or operator == "-" or operator == "x" or operator == "/":
        number2 = int(input("Type a number2: "))
    else:
        print("Operator not found. Please type correct operator")
        continue
    calculate(number1, number2, operator)
    print(f"{number1} {operator} {number2} = {result}")
    again = input(f"Do you want to calculate again with {result} or new calculate(y/n)?= ").lower()
    if again == "y":
        number1 = result
        continue
    elif again == "n":
        break

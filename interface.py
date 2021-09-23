from calculator import Calculator

print("Launching the calculator...")
stack = []
calc = Calculator()
user_input = ""
while user_input.lower not in ("exit", "q", "stop", "close"):
    user_input = input(">")
    stack.append(user_input)
    output = calc.calculate(user_input)
    print (stack)
    print(output)
print("Thank you for using the calulator... ")
print("Now closing the calculator")
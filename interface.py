import re
from calculator import Calculator

print("Launching the calculator...")
calc = Calculator()
user_input = ""
while user_input not in ("exit", "q", "stop", "close"):
    regex = re.search('[a-zA-Z]', user_input)
    if regex != None:
        print("Please write an expression")
    user_input = input(">")
    output = calc.calculate(user_input)
    print(output)
print("Thank you for using the calulator... ")
print("Now closing the calculator")

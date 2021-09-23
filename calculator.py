class Calculator:
    def calculate(self, input):
        global stack 
        user_input = input.split(" ")
        for y in user_input:
            if y.isdigit():
                stack.append(int(y))
            elif y == '+':
                if stack == []:
                    return "Can not add with out an interger"
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val1 + val2)
            elif y == '-':
                if stack == []:
                    return "Can not subtract with out an intergers"    
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
            elif y == '*':
                if stack == []:
                    return "There are no numbers in memory"
                stack.append(stack.pop() * stack.pop())
            elif y == '/':
                if stack == []:
                    return "There are no number in memory "
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 / val1)
        return stack 


import re
print("Launching the calculator...")
stack = []
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
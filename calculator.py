class Calculator:
    def calculate(self, input):
        global stack 
        user_input = input.split(" ")
        for y in user_input:
            if y not in ("-", "+", "*", "/","q", "clear", "c", ""):
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
exit = ("exit", "q", "stop", "close")
calc = Calculator()
user_input = ""
while user_input.lower() not in exit:
    regex = re.search('[a-zA-Z]', user_input)
    if user_input.lower() in ["c", "clear"]:
        stack = []
        print("The calculator is clearing...")
        print("The calculator is now clear")
    elif user_input in exit:
        print("Thank you for using the calulator... ")
        print("Now closing the calculator")
    elif regex != None:
        print("Please write an expression")
    user_input = input(">")
    output = calc.calculate(user_input)
    print(stack[-1])
print("Thank you for using the calulator... ")
print("Now closing the calculator")
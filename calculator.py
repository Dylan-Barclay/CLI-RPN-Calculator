class Calculator:
    def calculate(self, input):
        global stack
        user_input = input.split(" ")
        for input in user_input:
            if input.lower() not in ("-", "+", "*", "/", "exit", "q", "stop", "close", "clear", "c", ""):
                stack.append(int(input))
            elif input == '+' and len(stack)>1:
                if stack == []:
                    return "Can not add with out an interger"
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val1 + val2)
            elif input == '-' and len(stack)>1:
                if stack == []:
                    return "Can not subtract with out an intergers"    
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
            elif input == '*' and len(stack)>1:
                if stack == []:
                    return "There are no numbers in memory"
                stack.append(stack.pop() * stack.pop())
            elif input == '/' and len(stack)>1:
                if stack == []:
                    return "There are no number in memory"
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 / val1)
            elif input in ("exit", "q", "stop", "close"):
                print("Thank you for using the calulator... ")
                print("Now closing the calculator")
                break
            elif input == "":
                print()
            else:
                print("I am sorry this Calulator can not preform this action please try another")
        
        if len(stack) > 0:
            print(stack[-1])
        else:
            print()
        return stack 


import re
print("Launching the calculator...")
stack = []
calc = Calculator()
user_input = ""
while user_input.lower() not in ("exit", "q", "stop", "close"):
    regex = re.search('[a-zA-Z]', user_input)
    if user_input.lower() in ["c", "clear"]:
        stack = []
        print("The calculator is clearing...")
        print("The calculator is now clear")
    elif regex != None:
        print("Please write an expression")
    user_input = input(">")
    output = calc.calculate(user_input)
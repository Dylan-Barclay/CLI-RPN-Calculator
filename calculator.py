import re
class Calculator:
    def calculate(self, input):
        global stack
        input = input.split(" ")
        for action in input:
            if action.lower() not in ("-", "+", "*", "/", "exit", "q", "stop", "close", "clear", "c", "", ["a-z"]):
                stack.append(int(action))
            elif action == '+' and len(stack)>1:
                if stack == []:
                    return  "There are no numbers in memory"
                elif len(stack) < 1:
                    return "You need one more number to add please"
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val1 + val2)
            elif action == '-' and len(stack)>1:
                if stack == []:
                    return  "There are no numbers in memory"    
                elif len(stack) < 1:
                    return "You need one more number to add please"
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
            elif action == '*' and len(stack)>1:
                if stack == []:
                    return "There are no numbers in memory"
                elif len(stack) < 1:
                    return "You need one more number to add please"
                stack.append(stack.pop() * stack.pop())
            elif action == '/' and len(stack)>1:
                if stack == []:
                    return "There are no number in memory"
                elif len(stack) < 1:
                    return "You need one more number to add please"
                
                val1 = stack.pop()
                val2 = stack.pop()
                if val1 == 0:
                    return(f" You can not divide by zero... please try another number")
                stack.append(val2 / val1)
            elif action in ("exit", "q", "stop", "close"):
                print("Thank you for using the calulator... ")
                print("Now closing the calculator")
                return
            elif action == "":
                return
            else:
                return("I am sorry this Calulator can not preform this action please try another")
        
        if len(stack) > 0:
            print(stack[-1])
        else:
            print()
        return stack 


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
import re
class Calculator:
    def calculate(self, user_input):
        global memory 
        input = user_input.split(" ")
        for action in input:
            if action.lower() not in ("-", "+", "*", "/", "exit", "q", "stop", "close", "clear", "c","cls", ""):
                memory.append(int(action))
            elif action in ("-", "+", "*", "/") and len(memory) < 2:
                print("You need one more number to do this operation...")
                return
            elif action == '+' and len(memory)>1:
                val1 = memory.pop()
                val2 = memory.pop()
                memory.append(val1 + val2)
            elif action == '-' and len(memory)>1:
                val1 = memory.pop()
                val2 = memory.pop()
                memory.append(val2 - val1)
            elif action == '*' and len(memory)>1:
                memory.append(memory.pop() * memory.pop())
            elif action == '/' and len(memory) > 1:
                val1 = memory.pop()
                val2 = memory.pop()
                if val1 == 0:
                    print(" You can not divide by zero... please try another number")
                    return
                memory.append(val2 / val1)
            elif action in ("exit", "q", "stop", "close"):
                print("Thank you for using the calulator... ")
                print("Now closing the calculator")
                return
            elif action == "":
                return
            elif action in ("c", "clear", "cls"):
                return 
            else:
                print("I am sorry this Calulator can not preform this action please try another")
                print(" ")
                print("Calculator can only handle + - * / ")
                return 
        
        if len(memory) > 0:
            print(memory[-1])
        else:
            print()
        return memory 


print("Launching the calculator...")
print("")
print("  Clear: c, cls, clear     Exit: q, exit, stop, close")
print("")
memory  = []
calc = Calculator()
user_input = ""
while user_input.lower() not in ("exit", "q", "stop", "close"):
    regex = re.search('[a-zA-Z]', user_input)
    if user_input.lower() in ["c", "clear", "cls"]:
        stack = []
        print("The calculator is clearing...")
        print("The calculator is now clear")
    elif regex != None:
        print("Please write an expression")
    user_input = input(">")
    output = calc.calculate(user_input)
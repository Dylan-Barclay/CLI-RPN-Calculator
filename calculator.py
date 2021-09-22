class Calculator:
    def calculate(self, input):
        stack = []
        result = 0
        for x in input:
            if x.isdigit():
                stack.append(int(x))
            elif x == '+':
                if stack == []:
                    return "Can not add with out an interger"
                else:
                    result = stack.append(stack.pop() + stack.pop())
                    print (result) 
            elif x == '-':
                val1 = stack.pop
                val2 = stack.pop
                if stack == []:
                    return "Can not add with out an intergers"    
                else:
                    result = val2 - val1
            elif x == '*':
                result = stack.append(stack.pop() * stack.pop())
            elif x == '/':
                result = stack.append(val2 / val1)
        return result

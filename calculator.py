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
                    val1 = stack.pop()
                    val2 = stack.pop()
                    # print(val1)
                    # print(val2)
                    result = stack.append(val1 + val2)
                    # print (result) 
            elif x == '-':
                if stack == []:
                    return "Can not subtract with out an intergers"    
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    result = stack.append(val2 - val1)
            elif x == '*':
                result = stack.append(stack.pop() * stack.pop())
            elif x == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                result = stack.append(val2 / val1)
        return stack 

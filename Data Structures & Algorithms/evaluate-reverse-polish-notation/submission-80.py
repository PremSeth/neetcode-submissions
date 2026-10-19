class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def translate(a, b, func): 
            a = int(a)
            b = int(b)
            if func == "+": 
                return a + b
            if func == "*": 
                return a * b
            if func == "/": 
                print(a, b)
                if a < 0 and b > 0:
                    div = abs(a)//(b)
                    div = -1*div
                elif b < 0 and a > 0: 
                    div = a//abs(b)
                    div = -1*div
                else: 
                    div = a //b
                return div
            if func == "-":
                return a-b
        signs = set(['+', '-', '*', '/'])
        stack = []
        for i in tokens: 
            stack.append(i)
            if stack[-1] in signs: 
                sign = stack.pop()
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = translate(num2, num1, sign)
                stack.append(num3)
        return int(stack[-1])
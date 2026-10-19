class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = {'+', '-', '*', '/'}
        eval = []
        for i in tokens: 
            print(eval)
            if i not in signs: 
                eval.append(int(i))
            else: 
                if i == '+':
                    new_val = int(eval[-1])+int(eval[-2])
                    eval.pop()
                    eval.pop()
                    eval.append(new_val)
                if i == '-':
                    new_val = int(eval[-2])-int(eval[-1])
                    eval.pop()
                    eval.pop()
                    eval.append(new_val)
                if i == '*':
                    new_val = int(eval[-1])*int(eval[-2])
                    eval.pop()
                    eval.pop()
                    eval.append(new_val)
                if i == '/':
                    if (eval[-2] < 0 and eval[-1] > 0) or (eval[-2] > 0 and eval[-1] < 0):
                        new_val = abs(int(eval[-2]))//abs(int(eval[-1]))
                        new_val*=-1
                    else: 
                        new_val = int(eval[-2])//int(eval[-1])
                    eval.pop()
                    eval.pop()
                    eval.append(new_val)
        return eval[0]
        
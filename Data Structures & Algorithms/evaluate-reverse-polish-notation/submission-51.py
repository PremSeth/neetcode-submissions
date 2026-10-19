class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        functions = {
            "+": lambda x, y: int(x) + int(y),
            "-": lambda x, y: int(x) - int(y),
            "*": lambda x, y: int(x) * int(y),
            "/": lambda x, y: int(int(x) / (int(y)))
        }
        for i in tokens: 
            q.append(i)
            if q[-1] in "+*-/":
                sign = q[-1]
                q.pop()
                y = q.pop()
                x = q.pop()
                q.append(functions[sign](x, y))
        return int(q[-1])

        
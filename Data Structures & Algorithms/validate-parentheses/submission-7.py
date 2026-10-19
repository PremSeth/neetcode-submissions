class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(1)
            elif i == '{':
                stack.append(2)
            elif i == '[':
                stack.append(3)
            elif i == ')':
                if not stack: 
                    return False
                if not stack.pop() == 1:
                    return False
            elif i == '}':
                if not stack: 
                    return False
                if not stack.pop() == 2:
                    return False
            elif i == ']':
                if not stack: 
                    return False
                if not stack.pop() == 3:
                    return False
        if stack:
            return False
        return True 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        SIB = {"+", "-", "*", "/"}

        for s in tokens:
            if s in SIB:
                b = stack.pop()
                a = stack.pop()
                if s =='+':
                    stack.append(a + b)
                elif s =='-':
                    stack.append(a -b)
                elif s =='/':
                    stack.append(int(a / b))
                else:
                    stack.append(a * b)
            else:
                stack.append(int(s))
        
        return stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in s :
            if i in pair:
                if not stack:
                    return False
                
                if stack[-1] != pair[i]:
                    return False
                stack.pop()
            
            else :
                stack.append(i)
        return len(stack) == 0
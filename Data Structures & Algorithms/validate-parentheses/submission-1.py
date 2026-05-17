class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for ch in s:
            if ch in pair:
                if not stack or stack[-1] != pair[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return stack == [] 
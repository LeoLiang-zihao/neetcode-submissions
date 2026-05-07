class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dup = dict()
        if len(t) != len(s):
            return False
        for i in s:
            dup[i] = dup.get(i,0) + 1
        
        for i in t:
            if i not in dup or dup[i] == 0:
                return False
            dup[i] -= 1

        return True
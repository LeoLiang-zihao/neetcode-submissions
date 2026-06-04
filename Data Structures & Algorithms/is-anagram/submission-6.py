class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict1 = {}

        for i in s:
            dict1[i] = dict1.get(i,0) + 1

        for i in t:
            if i not in dict1:
                return False
            
            dict1[i] -= 1

            if dict1[i] < 0:
                return False
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False

        charseens = {}
        for char in s :
            charseens[char] = charseens.get(char,0) + 1
        
        charseent = {}
        for char in t :
            charseent[char] = charseent.get(char,0) + 1

        return charseens == charseent
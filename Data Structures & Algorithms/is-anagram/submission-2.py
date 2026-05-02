class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = dict()
        for char in s :
            seens[char] = seens.get(char,0) + 1
        
        seent = dict()
        for char in t :
            seent[char] = seent.get(char,0) + 1
        
        return seens == seent
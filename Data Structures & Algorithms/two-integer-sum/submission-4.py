class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Ans = {}

        for i , n in enumerate(nums):
            ans = target - n
        
            if ans in Ans:
                return [Ans[ans],i]
            else:
                Ans[n] = i
        
        
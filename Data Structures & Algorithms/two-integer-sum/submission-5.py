class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seenlist = {}
        for i ,n in enumerate(nums):
            ans = target - n

            if ans in seenlist:
                return [seenlist[ans],i]
            else:
                seenlist[n] = i
        
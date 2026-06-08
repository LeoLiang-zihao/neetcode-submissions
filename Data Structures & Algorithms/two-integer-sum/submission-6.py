class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            ans = target - nums[i]

            if ans in dicts:
                return [dicts[ans] , i]
            else:
                dicts[nums[i]] = i
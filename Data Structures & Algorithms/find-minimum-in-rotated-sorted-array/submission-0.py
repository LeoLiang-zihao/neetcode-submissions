class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        def in_in_right_part(i):
            return nums[i] <= last
        

        left , right = 0,len(nums) -1
        while left < right:
            mid = (left + right) //2
            if in_in_right_part(mid):
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
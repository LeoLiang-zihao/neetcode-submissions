class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #首先可以先从一个list开始遍历，假设我们能记住过去的数字
        #key 里面放过去的当前的数字，假如当前的 target - num = 过去的数字
        #就取对应的位置也就是value
        seen = {} 
        for i , num in enumerate(nums) :
            AS = target - num
            
            if num in seen:
                return[seen[num] , i] 
            else:
                seen[AS] = i

        return []


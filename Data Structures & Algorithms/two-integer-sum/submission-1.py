class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_answer = {}
        for i , num in enumerate(nums):
            AS = target - num
            
            if num in seen_answer:
                
                return [seen_answer[num],i]
            else :
                seen_answer[AS] = i

        return []
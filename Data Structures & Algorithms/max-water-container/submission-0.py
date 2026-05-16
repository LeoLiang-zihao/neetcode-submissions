class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1 
        ans = 0
        while left < right:
            hight = min(heights[left],heights[right])
            width = right - left

            area = hight * width

            ans = max(area, ans)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return ans
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i in prices[1:]:
            profit = i - minprice
            maxprofit = max(maxprofit,profit)
            minprice = min(i,minprice)
        
        return maxprofit
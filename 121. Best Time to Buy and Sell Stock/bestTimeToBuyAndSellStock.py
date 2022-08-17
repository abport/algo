# Complexity ---------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 1 # l=Buy, r=Sell
        maxPrice = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxPrice = max(maxPrice, profit)
            else: 
                l = r
            r += 1
        
        return maxPrice
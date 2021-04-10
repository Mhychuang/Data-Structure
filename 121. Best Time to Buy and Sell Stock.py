class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
    
        cur_min, profit = float('inf'), 0
        
        for p in prices:
            cur_min = min (p, cur_min)
            profit = max (profit, p-cur_min)
        return profit
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_purchase = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_purchase:
                min_purchase = prices[i]
            
            if (prices[i] - min_purchase) > max_profit:
                max_profit = prices[i] - min_purchase
        
        return max_profit


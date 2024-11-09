class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price=float(inf)
        max_profit=0
        for price in prices:
            min_price=min(min_price, price)
            profit_temp= price-min_price
            max_profit=max(max_profit, profit_temp)
        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] #price to buy 
        max_profit = 0 #profit starts from 0

        for price in prices:
            if price < min_price:
                min_price = price    #found cheaper day to  buy

            else:
                profit = price - min_price #sell today
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
        
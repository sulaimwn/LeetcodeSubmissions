class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1
        max_profit = 0

        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                # if it is a profitable window check to see if its worth storing to top
                max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
            else:
                #in this case, we arent even in a profitable window
                #so we move the buy day to sell day
                # and sell day increases by 1
                #this is the only time we move buy day
                buy_day=sell_day
                #we set buyday to sellday bcs its the smallest leftest num we seen so far

            sell_day += 1
        return max_profit


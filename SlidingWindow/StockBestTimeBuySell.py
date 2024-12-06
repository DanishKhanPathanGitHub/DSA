"""
121. Best Time to Buy and Sell Stock
You are given an array prices where 
prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

#so we will actually have to keep track which day at price of stock is least 
#we subtract that price from current day stock price, to calc the profit
#if profit is > current profit which we will keep track of, 
# we will update the profit
#But also we need to update the lowest price if we found new lowest price
def maxProfit(self, prices: list[int]) -> int:
    res = 0
    lowest = prices[0]
    if len(prices) == 1:
        return 0
    for i in range(1, len(prices)):
        profit =  prices[i] - lowest
        res = max(profit, res)
        if prices[i] <= lowest:
            lowest = prices[i]
    return res

#what we do here is, for ex. [7,1,5,3,6,4]...
#7 lowest, 1, 1-7 = -6 < current profit.
#1 < 7 so we update the current low price of stock
#for 1, we go deep and calc profit
#untill we find more less price than 1
#here 1 is just ex, any value, we go deep into that
#this make the process linear 
#this is window sliding, keeping one point to track on 
# and go deep untill next window found / 
# low or high according to problem

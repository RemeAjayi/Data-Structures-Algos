#Best time to buy and sell stock from blind 75 and asked in Capital one data science assessment
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #if r > l, then r = r + 1 and left = r
    #store max on every subtraction only update max if it's greater than previous max
        maxP = 0
        l,r = 0,1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1 
        return maxP
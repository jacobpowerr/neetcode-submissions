class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            profit = max(profit, curr_profit)

            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1

        return profit
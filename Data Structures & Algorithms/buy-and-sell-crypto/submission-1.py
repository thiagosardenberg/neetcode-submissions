class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profits = []
        while r < len(prices):
            if prices[l] < prices[r]:
                profits.append(prices[r] - prices[l])
                r += 1
            elif prices[r] <= prices[l]:
                l = r
                r += 1
        if profits:
            return max(profits)
        else:
            return 0

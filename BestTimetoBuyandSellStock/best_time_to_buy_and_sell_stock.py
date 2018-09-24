class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]:
            return 0
        mini = prices[0]
        days = len(prices)
        diff = [0] * days
        for i in range(1, days):
            if prices[i] <= mini:
                mini = prices[i]
            else:
                diff[i] = prices[i] - mini
        return max(diff)

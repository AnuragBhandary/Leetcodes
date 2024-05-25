class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = 0
        minimum = prices[0]

        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > maxdiff:
                maxdiff = prices[i] - minimum

        return maxdiff

        
        # maxdiff = 0

        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j]- prices[i] > maxdiff:
        #             maxdiff = prices[j] - prices[i]

        # return maxdiff

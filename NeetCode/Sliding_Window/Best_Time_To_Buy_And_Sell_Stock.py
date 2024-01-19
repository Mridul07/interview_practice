class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1 #Pointers
        maxP = 0
        currP = 0
        while r < len(prices):
            currP = prices[r] - prices[l]
            if currP > maxP:
                maxP = currP
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return maxP
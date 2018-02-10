#like dp: the max-profit prof[i] if you sell at i
# maintain the min-price so far, prof[i]=price[i]-min_price
# then we got a array of the profit you sold at each point, max(l) got the answer 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:
            return 0
        profit=[]
        min_price=float("inf")
        for i in range(len(prices)):
            min_price=min(prices[i],min_price)
            profit.append(prices[i]-min_price)
        return max(profit)
            
            
        
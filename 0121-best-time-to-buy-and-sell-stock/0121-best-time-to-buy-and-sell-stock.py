class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        p=0
        for i in range(1,len(prices)):
            c=prices[i]-min_price
            p=max(c,p)
            min_price=min(min_price,prices[i])
        return p



        
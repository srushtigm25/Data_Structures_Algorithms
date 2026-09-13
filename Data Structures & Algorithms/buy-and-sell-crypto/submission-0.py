class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l= 0
        # maxpr = 0 

        # for r in range(1,len(prices)):
        #     if prices[l] < prices[r]:
        #         maxpr = max(maxpr, prices[r]-prices[l])
        #     else:
        #         l=r
        #     r+=1
        # return maxpr

        minp = prices[0]
        maxp = 0

        for currp in prices:
            if currp < minp:
                minp = currp
            profit = currp - minp

            if profit > maxp:
                maxp = profit
        return maxp



        
            


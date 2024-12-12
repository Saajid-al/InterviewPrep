class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0        
        for r in range(len(prices)): #iterate through the prices
            maxP = max(maxP, prices[r] - prices[l]) # we find the max price of the stocks
            if prices[l] > prices[r]: #update our left pointer if we do end up finding a new low
                l = r
            
        return maxP
    
s = Solution()
print(s.maxProfit([2,5,7,1,2,4]))
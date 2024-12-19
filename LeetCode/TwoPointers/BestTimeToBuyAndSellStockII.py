class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxP += prices[i] - prices[i-1]
        return maxP

#dp ?

s = Solution
print(s.maxProfit([1,3,5,1,2]))
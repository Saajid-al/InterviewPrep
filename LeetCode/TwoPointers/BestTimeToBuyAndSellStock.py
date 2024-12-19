from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        l = 0 
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            if prices[r]-prices[l] > 0:
                maxP += prices[r] - prices[l]
                l+=1
            

        return maxP

        #add to the hashmap with index and values ? 
        #got 7 expected 8.
        #1
        #[3,3,5,0,0,3,1,4]
                    #L 
                        #R


def main():
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))


if __name__ == "__main__":
    main()
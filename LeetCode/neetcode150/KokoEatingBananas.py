from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1 #NOTE WE START AT 1 SO WE AVOID DIVISION AT 0
        r = max(piles) #get the max number
        minK = r #getting the max value that koko can eat
        while(l<=r): 
            mid = l + (r - l) // 2 #get mid value
            hours = 0
            for banana in piles: #here's where it gets tricky. We want to compute the amount of hours it would take koko to consume the pile
                hours += math.ceil(banana/mid) #we divide it by the value, and we use math.ceil to round up
            
            if hours <= h: #if there exists a smaller element, we want to explore 
                minK = min(minK, mid) #we computer the minimum value
                r = mid - 1
            else:
                l = mid + 1 

        return minK                

s = Solution()
print(s.minEatingSpeed([3,6,7,11]), 8)

         
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        res = []
        n = len(potions)
        for s in spells:
            if s * potions[-1] < success:
                res.append(0)
                continue
            l = 0 
            r = len(potions)-1

            while(l <= r):
                mid = l + (r-l) // 2 

                if potions[mid] * s >= success: #maybe we can find a smaller val
                    r = mid - 1 
                elif potions[mid] * s < success:
                    l = mid + 1 


            res.append(n-l)

        return res

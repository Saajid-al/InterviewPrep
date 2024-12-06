from collections import defaultdict
import collections


class Solution:
    def totalFruit(self, fruits) -> int:
        l = 0
        r = 0
        basket = collections.defaultdict(int)
        total = 0
        res = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1 
            total += 1 

            while len(basket) > 2:
                f = fruits[l]
                basket[f] -= 1 
                total-=1
                l+=1
                if not basket[f]:
                    basket.pop(f)

            res = max(res, total)
        return res
            

       
s = Solution()
print(s.totalFruit([0,1,2,2]))
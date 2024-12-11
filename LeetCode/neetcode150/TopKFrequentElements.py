from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #We use the Bucket Sorting Algorithim
        count = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)] # why + 1 ? 
        #creating buckets [[],[],[]] <- example 
        res = []
        for i in nums:
            count[i] +=1 

        for c,v in count.items():
            bucket[v].append(c)
        print(c)
        for i in range(len(bucket) - 1, 0, -1):
            for x in bucket[i]:
                res.append(x)
                if len(res) == k:
                    return res    
        return res        
                    

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3,9,6,5,6,1], 2))
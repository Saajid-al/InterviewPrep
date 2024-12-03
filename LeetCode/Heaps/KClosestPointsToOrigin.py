class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        for (x,y) in points:
            distance = (x**2)+(y**2)
            res.append([distance, x,y])

        heapq.heapify(res)
        result = []
        while(k > 0):
            dist, x , y = heapq.heappop(res)
            result.append([x,y])
            k-=1

        return result
    

s = Solution()
print(s.kClosest([[1,3],[-2,2]]))
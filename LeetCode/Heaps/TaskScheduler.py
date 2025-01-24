import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks, n):
        hashmap = {}

        for t in tasks:
            if t in hashmap:
                hashmap[t] += 1
            else:
                hashmap[t] = 1


        #Queue[(3, 1)]
        maxHeap = [-cnt for cnt in hashmap.values()]

        heapq.heapify(maxHeap)
        time = 0    
        queue = collections.deque()

        while(maxHeap or queue):

            time+=1

            if maxHeap: #if we have a heap
                current = 1 + heapq.heappop(maxHeap) #we're adding one to determine that we've taken one "time"
                if current:
                    queue.append([current, time+n]) #we'd want to add however much time + the current amount of time until it's empty
                
            if queue and queue[0][1] == time:
                    heapq.heappush(maxHeap, queue.popleft()[0])
        return time
            

            





s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))
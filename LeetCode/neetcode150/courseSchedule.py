from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        
        preReq = defaultdict(list)

        for pre, course in prerequisites:
            preReq[pre].append(course)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.append(node)
        dfs(numCourses)
            
            

s = Solution()
print(s.canFinish([[1,0],[0,1]]))
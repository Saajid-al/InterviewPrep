from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b) 
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if g[crs] == []: #if there is no prerequisites, lets return an empty list
                return True
            visitSet.add(crs)
            for pre in g[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            g[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

def main():
    s = Solution()
    s.canFinish(2, [[1,0],[0,1]])


if __name__ == "__main__":
    main()
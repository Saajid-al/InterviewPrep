from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        rows = len(prerequisites)
        cols = len(prerequisites[0])
        preReq = defaultdict(list)
        for c, p in prerequisites:
            preReq[c].append(p)

        seen = set()
        def cycle(course, seen):
            if course in seen:
                return True
            seen.add(course)
            for p in preReq[course]:
                if cycle(p, seen):
                    return True
            preReq[course] = []
            seen.remove(course)
            return False


        for course in range(numCourses):
            if cycle(course, seen):
                return False
        return True


def main():
    s = Solution()
    s.canFinish(2, [[1,0],[0,1]])


if __name__ == "__main__":
    main()
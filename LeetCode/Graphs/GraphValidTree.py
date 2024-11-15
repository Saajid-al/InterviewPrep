from collections import defaultdict

class Solution(object):
    def validTree(self, n,edges):
        if not n:
            return True

        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def dfs(i,prev):
            if i in visited:
                return False
            visited.add(i)
            for j in graph[i]:
                if j==prev:#we're in the same loop? 
                    continue
                if not dfs(j, i):
                    return False
            return True
                    
        return dfs(0, -1) and n == len(visited)

s = Solution()
print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
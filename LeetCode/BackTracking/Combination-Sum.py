class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        target = target
        res = []
        sol = []
        def dfs(i):
            if i >= N:
                for j in sol:
                    temp += j 
                if j == self.target:
                    res.append(sol)
                else:
                    return
        
            sol.append(candidates[i])
            dfs(i+1)


            sol.pop()
            dfs(i+1)
            
        dfs(0)
        return res
def main():
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
if __name__ == "__main__":
    main()

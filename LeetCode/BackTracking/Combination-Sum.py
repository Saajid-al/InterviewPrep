class Solution:
    def combinationSum(self, candidates, target):
        target = target
        res = []
        subSet = []

        def dfs(i):

            if sum(subSet) == target:
                res.append(subSet.copy())
                return

            if sum(subSet) > target or i >= len(candidates):
                return
            subSet.append(candidates[i])
            dfs(i) 

            subSet.pop()
            dfs(i+1)
            
        dfs(0)
        return res

def main():
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))

if __name__ == "__main__":
    main()

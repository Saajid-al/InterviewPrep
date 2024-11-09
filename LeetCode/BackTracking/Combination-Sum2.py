class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        candidates.sort()
        def dfs(i):

            if sum(subSet) == target:
                res.append(subSet.copy())
                return
            if sum(subSet) > target or i>=len(candidates):
                return 

            subSet.append(candidates[i])
            dfs(i+1)

            subSet.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1)

        dfs(0)
        return res

def main():
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))


if __name__ == "__main__":
    main()

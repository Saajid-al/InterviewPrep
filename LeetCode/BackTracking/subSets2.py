class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []
        nums.sort()
        def dfs(i):

            if i >= len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            dfs(i+1)

            subSet.pop()
            while(i+1 < len(nums) and nums[i]==nums[i+1]):
                i+=1

            dfs(i+1)
        dfs(0)
        return res
def main():
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))


if __name__ == "__main__":
    main()


# [[4,4,4,1,4],[4,4,4,1],[4,4,4,4],[4,4,4],[4,4,1,4],[4,4,1],
#  [4,4],[4,1,4],
#  [4,1],[4],[1,4],[1],[]]

# [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4]
#  ,[4],[4,4],[4,4,4],[4,4,4,4]]
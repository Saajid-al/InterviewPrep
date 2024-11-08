class Solution():
    def subsets(self, nums):
        res = []
        subSet = []
        def dfs(i): #i being the index
            if i >= len(nums): #basecase
                res.append(subSet.copy())
                return
            #decision to include nums[i]

            subSet.append(nums[i])
            dfs(i+1)

            #decision not to include nums[i]
            subSet.pop()
            dfs(i+1)

        dfs(0)
        return res

def main():
    s = Solution()
    print(s.subsets([1,2,3]))


if __name__ == "__main__":
    main()
class Solution:
    def permute(self, nums):
        
        res = []
        subSet = []
        def dfs(i):
            
            if len(subSet) == len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            dfs(i+1)

            subSet.pop()
            dfs(i+1)

        dfs(0)  
        return res



def main():
    s = Solution()
    print(s.permute([1,2,3]))


if __name__ == "__main__":
    main()
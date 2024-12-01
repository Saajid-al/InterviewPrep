class Solution:
    def singleNonDuplicate(self, nums):
        l = 0 
        r = len(nums) - 1 

        while(l < r): 
            m = l + (r-l) // 2 
            print(m,"nums = : ", nums[m])
            
            if (m - 1 < 0 or nums[m] != nums[m-1]) and (nums[m+1] != nums[m] or m == len(nums)):
                return nums[m]
            
            leftSize = m - 1 if nums[m-1] == nums[m] else m

            if leftSize % 2:
                r = m-1 
            else : 
                l = m + 1 


s = Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
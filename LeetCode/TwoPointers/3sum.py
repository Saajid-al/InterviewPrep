class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums)-1
        res = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:#check current position if it's equal to last to make sure we can skip
                continue
            l = i+1 # reset left pointer
            while (l<r): # while our left pointer is less than our right (went through all combinations)
                if val + nums[l] + nums[r] > 0: #shift the highest pointer down
                    r-=1
                elif val + nums[l] + nums[r] < 0: #increase the lower pointer by 1
                    l+=1
                else:
                    res.append([val, nums[l], nums[r]]) #we're at 0, append it to our list and go to the next val
                    l+=1
                while(l < r and nums[l] == nums[l-1]): #while our left pointer and previous is the same we can start skipping
                    l+=1
        return res


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
#[-4,-1,-1,0,1,2]
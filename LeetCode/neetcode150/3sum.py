class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)): #iterate through
            if i > 0 and nums[i-1] == nums[i]: #here's where we can take care of the duplicates
                continue

            l = i+1
            r = len(nums)-1
            while (l<r): #typical two pointer search
                val = nums[i] + nums[l] + nums[r]
                if val > 0: #if greater than the target, all we need to do is update the right pointer down
                    r-=1
                elif val < 0: #update the left pointer by 1
                    l+=1
                else:  #we found our targert
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while(nums[l-1] == nums[l] and l < r): #get rid of more duplicates
                        l+=1

        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
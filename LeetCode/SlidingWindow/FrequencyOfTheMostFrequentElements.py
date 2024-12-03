class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        r = 0
        total = 0
        l = 0
        maxTotal = 0
        while r < len(nums):
            total += nums[r]

            while (nums[r] * (r - l + 1)> total + k):
                total-=nums[l]
                l+=1
            
            maxTotal = max(maxTotal, r - l + 1 )
            r+=1

        return maxTotal
            
        #go through each elemeent, try and see how many duplicates we can create
        #start by usng r. Then we do, while r<=len(nums):

        
s = Solution()
print(s.maxFrequency([1,2,4], 5))
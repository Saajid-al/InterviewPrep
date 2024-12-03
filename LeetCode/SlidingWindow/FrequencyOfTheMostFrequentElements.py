class Solution:
    def maxFrequency(self, nums, k):
        maxFreq = 0
        l = 0
        temp = 0
        tempK = 0
        i = 0
        r = 0
        for r in range(len(nums)-1):
            tempK= k
            l = r 
            while l >= 0 and tempK >= 0:
                if nums[l] != nums[r]:
                    if tempK + nums[l] >= k:
                        tempK -= nums[r] #5-2 = 3 
                    if tempK < 0:
                        break
                maxFreq = max(maxFreq, r - l + 1)
                l-=1
            
        return maxFreq

            
        #go through each elemeent, try and see how many duplicates we can create
        #start by usng r. Then we do, while r<=len(nums):

        
s = Solution()
print(s.maxFrequency([1,2,4], 5))
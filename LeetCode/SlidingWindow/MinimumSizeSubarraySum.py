class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        l = 0
        sumOfSub = 0
        minLength = len(nums)
        flag = False
        for r in range(len(nums)):
            sumOfSub+=nums[r]
            while(sumOfSub >= target): #we want to shift our sliding window
                flag = True
                minLength = min(minLength, r-l+1)
                sumOfSub-=nums[l]
                l+=1

        return minLength if flag==True else 0
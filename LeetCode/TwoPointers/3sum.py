class Solution(object):
    def threeSum(self, nums):
        #arr = [] * nums
        results = []
        nums.sort()
        for i, val in enumerate(nums) :
            if i > 0 and val == nums[i-1]: #once its sorted, we check if the next index, is equal to the previous(so we can skip)
                continue
            l, r = i + 1, len(nums) - 1 
            while l < r :
                if val + nums[l] + nums[r] > 0:  #if its greater than the largest right pointer, decrease right
                    r -= 1 
                elif val + nums[l] + nums[r] < 0: #if it's too low, increase left pointer
                    l += 1 
                else:
                    results.append([val,nums[l], nums[r]])
                    l+= 1
                    while nums[l] == nums[l-1] and l < r :
                        l+=1
        return results
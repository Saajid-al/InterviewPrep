from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr = [1] * len(nums)
        accumulator = 1 

        for i in range(len(nums)):
            arr[i] = accumulator
            accumulator = nums[i] * accumulator

        accumulator2 = 1 
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= accumulator2
            accumulator2 *= nums[i] 

        return arr


s = Solution()
print(s.productExceptSelf([1,2,3,4]))
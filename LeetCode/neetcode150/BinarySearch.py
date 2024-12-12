from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums)-1

        while(l<=r): #while l<=r we use <= because the target may be in the middle.
            mid = l + (r-l) //2 #prevent overflow. Calculating mid
            if nums[mid] == target: #if the middle index is equal to the target
                return mid #we would want to return the mid index
            elif nums[mid] > target: #if it's greater than the index, we would want to update the right pointer to the middle - 1 
                r = mid-1
            elif nums[mid] < target: #same for left pointer
                l = mid + 1 

        return -1

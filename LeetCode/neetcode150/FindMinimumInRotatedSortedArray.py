class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minimum = nums[0]

        while(l<=r): #classic binary search
            if nums[l] < nums[r]: #if we find ourselves at a point where nums[r] is greater than nums[l], we've found our pivot point (array is sorted)
                minimum = min(minimum, nums[l]) #calculate minimum
                break
            mid = l + (r-l) // 2 
            minimum = min(minimum, nums[mid]) 
            if nums[mid] >= nums[l]: #if we're in ascending order, that means the minimum value would be to the right
                l = mid + 1  
            else:
                r = mid - 1 #if not, it would be in the left 
        return minimum
    
s = Solution()
print(s.findMin([3,4,5,1,2]))
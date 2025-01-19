class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def valid(boundary):
            
            i = 0
            count = 0

            while(i<len(nums)-1):
                if abs(nums[i] - nums[i+1]) <= boundary:
                    i+=2
                    count+=1
                else:
                    i+=1
                if count == p:
                    return True

            return False
        
        if p == 0:
            return 0

        nums.sort()
        l = 0 
        r = nums[len(nums)-1]
        
        res = 0

        while(l<=r):
            m = l + (r-l) // 2 

            if valid(m):
                res = m
                r = m-1
            else:
                l = m+1 
        return res






















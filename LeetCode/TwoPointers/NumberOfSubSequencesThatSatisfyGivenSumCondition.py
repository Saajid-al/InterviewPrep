class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums)-1
        numSubSeq = 0
        min_ele = nums[0]
        max_ele = nums[0]

        for r in range(len(nums)-1):
            max_ele = max(max_ele, nums[r])
            min_ele = min(nums[l], min_ele)

            if min_ele + max_ele >= 9:
                l+=1
            numSubSeq+=1

            
        return numSubSeq

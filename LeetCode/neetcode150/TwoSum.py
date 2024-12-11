class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)): #iterate through the list
            if target - nums[i] in hashmap : #if the complement exists in the hashmap, we want to return
                return [ i, hashmap[target-nums[i] ]] #return both indexes
            else:
                hashmap[nums[i]] = i #add to the hashmap, if a complement doesnt exist
s = Solution()
print(s.twoSum([2,7,11,15], 9))
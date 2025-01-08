class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, hashset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for num in hashset:
                if hashset[num] > 0:
                    subset.append(num)
                    hashset[num]-=1
                    backtrack(subset, hashset)
                    subset.pop()
                    hashset[num]+=1
        backtrack([], Counter(nums))
        return res
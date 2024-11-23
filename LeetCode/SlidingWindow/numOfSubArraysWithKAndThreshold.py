class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = 0
        subArr = 0
        sum = 0  

        for r in range(len(arr)):
            sum += arr[r]

            if r - l + 1 == k:
                if sum / k >= threshold:
                    subArr += 1
                sum -= arr[l]
                l += 1

        return subArr
                

s = Solution()
print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3))
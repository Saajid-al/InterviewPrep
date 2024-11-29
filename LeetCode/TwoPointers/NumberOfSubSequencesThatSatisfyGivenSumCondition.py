class Solution:
    def numSubseq(self, nums, target):
        nums.sort()

        l = 0 
        r = len(nums)-1
        res = 0
        mod = int(10 ** 9 + 7)
        for l in range(len(nums)):
            while nums[l] + nums[r] > target and r>=l:
                r-=1
            if r>=l :
                res += (2**(r-l))
                res %= mod
            
        return res

def main():
    s = Solution()
    print(s.numSubseq([3,5,6,7], 9))
if __name__ == "__main__":
    main()
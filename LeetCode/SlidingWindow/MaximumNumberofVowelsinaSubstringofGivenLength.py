class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        vowels = ["a", "e", "i", "o", "u"]
        maxLen = 0
        cnt=0

        for r in range(len(s)):
            if s[r] in vowels:
                cnt+=1
            if r-l+1 > k:
                if s[l] in vowels:
                    cnt-=1
                l+=1
            maxLen = max(maxLen, cnt)
        return maxLen


s = Solution()
print(s.maxVowels("abciiidef", 3))
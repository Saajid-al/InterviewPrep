class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s)-1
        
        while(l<=r):
            if s[l]!=s[r]:
                sLeft, sRight = s[l+1:r+1], s[l:r]
                return sLeft == sLeft[::-1] or sRight == sRight[::-1]
            l+=1
            r-=1
        return True
    
s = Solution
print(s.validPalindrome("AAVA"))
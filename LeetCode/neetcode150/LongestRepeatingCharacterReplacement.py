class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        maxLen = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #create a dicitonary of the count of each letters
            while r-l+1 - max(count.values()) > k: #if the window - max(freq char value) is greater than K
                count[s[l]]-=1 #reduce the counter index by 1
                l+=1 #shift our pointer
            maxLen = max(maxLen, r-l+1) #get maxLength

        return maxLen


s = Solution()
print(s.characterReplacement("AABABBA", 1))
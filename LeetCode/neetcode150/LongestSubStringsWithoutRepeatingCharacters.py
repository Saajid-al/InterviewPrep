class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = []
        l = 0
        maxLen = 0
        for r in range(len(s)): #iterate
            while(s[r] in hashSet): #if we found a repeating character
                hashSet.remove(s[l]) #we would like to remove it
                l+=1 #keep removing until the character no longer exists
            hashSet.append(s[r]) #add the new character if it is not in the hashSet
            maxLen = max(maxLen, len(hashSet)) #get the length of the string

        return maxLen

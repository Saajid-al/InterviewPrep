class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        for x in s : 
            if s.count(x) != t.count(x):
                return False
        return True
    

s = Solution()
print(s.isAnagram("anagaram", "nagaram"))
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        hashmap = defaultdict(list)
        count = [0]*26
        for x in s1:
            count[ord(x) - ord("a")]+=1
        hashmap[tuple(count)].append(s1)

        freq = [0]*26
        for r,val in enumerate(s2): #for every letter in s2
            freq[ord(val) - ord("a")]+=1 #count the number of frequent characters, after every iteration

            while r-l > len(s1)-1: #while the window is the same as s1
                freq[ord(s2[l]) - ord("a")] -= 1  #delete the left pointer value
                l+=1 #increment left pointer

            if r-l+1 == len(s1) and tuple(freq) in hashmap: #checking if it exists in the hashmap. Note we can only check immutable lists in a hashmap
                    return True
                    

        return False

s = Solution()  
print(s.checkInclusion("ab", "eidbaooo"))  # Should return True, "ab" = "ba" 

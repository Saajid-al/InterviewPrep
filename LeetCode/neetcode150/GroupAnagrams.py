from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) #we use a defaultdict in order to access elements that don't already exist
        
        for s in strs:
            count = [0] * 26 #create a list of possible letters (26 letters in the alphabet) mapped by their ord values
            for letter in s: 
                count[ord(letter)  - ord("a")] += 1 #mapping a -> 1, b - > 2 etc. Technically you can do ord[letter] with the ord list being 1000
            hashmap[tuple(count)].append(s) #LISTS CANNOT BE APPENDED AS KEYS SINCE THEY ARE MUTABLE. That's why we use tuple
        return list(hashmap.values()) #we return a lits of all the hashmap values for the solution
    

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        n = Counter(s)
        hashmap = defaultdict(list)
        for char, cnt in n:
            hashmap[cnt].append(char)
        print(n)

s = Solution()
print(s.frequencySort("tree"))
from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s):
        n = Counter(s)
        hashmap = defaultdict(list)
        for char, cnt in n.items():
            hashmap[cnt].append(char)

        for i in range(len(s), 0 , -1):
            for c in hashmap[i]:
                res += c * i
        return res            


s = Solution()
print(s.frequencySort("tree"))
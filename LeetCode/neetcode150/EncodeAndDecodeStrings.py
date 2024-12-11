from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = ""
        i = 0

        while i<len(s):
            j = i
            while j!="#":
                j+=1
            length = int(str[i:j]) #this accounts for double digits. i - j for example 45#. i-j returns 45
            res.append(str[j+1:j+1+length])
            i = j + 1 + length
        return res
# i 
#4neet, #4code, #4love, #3you

s = Solution()
print(s.encode(["neet","code","love","you"]))
print(s.decode("4#neet4#code4#love3#you"))
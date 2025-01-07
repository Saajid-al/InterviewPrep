class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        curr = ""
        multiplier = 0
        for char in s:
            if char.isdigit():
                multiplier = multiplier*10 + int(char)
            elif char == "[":
                stack.append((curr, multiplier))
                curr = ""
                multiplier = 0
            elif char == "]":
                    res, multi = stack.pop()
                    curr = res + curr * multi
            else:
                curr += char
        return curr



    

    
s = Solution()
print(s.decodeString("3[a]2[bc]"))
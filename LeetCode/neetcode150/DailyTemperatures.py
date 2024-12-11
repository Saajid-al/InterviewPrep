from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]: # we found an element that is larger than our previous element. .. We do a while looop, as this also gives the answer to elements that we didn't have the answer to earlier.
                stackT, stackIndex = stack.pop() #grabbing the stack value and index
                res[stackIndex] = i - stackIndex #setting the element that we didn't have before to it's index.

            stack.append([val, i]) #append the value, and it's index at i

        return res
s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
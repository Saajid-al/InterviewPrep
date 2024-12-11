from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        res = []
        subSet = ""
        openB = 0
        closeB = 0
        def dfs(subSet, openB, closeB): 
            if openB == closeB == n: #our base case, if the opening brackets match with the closing brackets, and we have n pairs.
                res.append(subSet) #we can append this to our result
            
            if closeB < openB: #if there exists an open bracket, that doesn't have matching close bracket yet
                dfs(subSet + ")", openB, closeB+1) #append it to our subset
            if openB < n: #while we can still add open brackets. We need to have n pairs
                dfs(subSet+"(", openB+1, closeB) #we add an open bracket. 

        dfs(subSet, openB, closeB)
        return res
s = Solution()
print(s.generateParenthesis(3))
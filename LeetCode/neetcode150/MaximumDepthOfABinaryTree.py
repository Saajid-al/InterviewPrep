class TreeNode:
    def __init__(self, val = 0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:

        def dfs(root, depth):

            if not root:
                return depth

            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))

        
        return dfs(root, 0) 


a = TreeNode(5)
b = TreeNode(6)
c = TreeNode(7)
a.left = b
a.right = c

s = Solution()
print(s.maxDepth(a))
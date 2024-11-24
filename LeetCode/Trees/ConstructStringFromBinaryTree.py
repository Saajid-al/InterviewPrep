class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        def dfs(root):

            if not root:
                return
                
            self.res +=  "(" +  str(root.val)  
            
            if not root.left and root.right:
                self.res+="()"


            dfs(root.left)
            dfs(root.right)
            self.res+= ")"
        dfs(root)
        return self.res[1:-1]


        dfs(root)
        return self.res

            
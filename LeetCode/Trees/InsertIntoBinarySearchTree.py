# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = val
        self.newVal = TreeNode(self.val)
        def insert(root):
            if not root :
                return self.newVal
            if self.val >= root.val:
                if root.right is None:
                    root.right = self.newVal
                else:
                    insert(root.right)
            elif self.val < root.val:
                if root.left is None:
                    root.left = self.newVal
                else:
                    insert(root.left)
            return root
        return insert(root)
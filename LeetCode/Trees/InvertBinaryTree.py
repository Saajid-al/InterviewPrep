class TreeNode(object):
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        
        def dfs(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
            return root
        return dfs(root)
    def printBST(self, root):
        if not root:
            return
        print(root.val)
        self.printBST(root.left)
        self.printBST(root.right)


def main():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.left = b
    a.right = c

    s = Solution()
    s.printBST(a)
    s.printBST(s.invertTree(a))

if __name__ == "__main__":
    main()
from typing import List, Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        level = []
        res = []

        while(queue):
            level.append(queue)
            nRoot = queue.pop()
            while(nRoot):
                queue.append(nRoot.left)
                queue.append(nRoot.right)
            if level:
                res.append([level])
            level.pop()

        return res
    
def main():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    s = Solution()
    print(s.levelOrder([3,9,20,None,None,15,7]))


if __name__ == "__main__":
    main()
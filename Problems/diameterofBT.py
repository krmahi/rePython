
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# recursive DFS
class solution:
    def diameter(self, root:Optional[TreeNode]) -> int:
        res = 0

        def maxheight(root):
            nonlocal res

            if not root: return 0
            left = maxheight(root.left)
            right = maxheight(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        maxheight(root)
        return res
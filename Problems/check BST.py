import sys
import TreeNode as Tree
from typing import Optional

class solution:
    def validBST(self, root:Optional[Tree.TreeNode]) -> bool:
        def checkBST(root, minval, maxval):
            if not root: return True
            if root.val >= maxval or root.val <= minval: return False
            return checkBST(root.left, minval, root.val) and checkBST(root.right, root.val, maxval)
        return checkBST(root, -sys.maxsize - 1, sys.maxsize)
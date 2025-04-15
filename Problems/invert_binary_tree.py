from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        if left or right: root.left, root.right = root.right, root.left
        return root
from typing import Optional

class TreeNode:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

class solution:
    def maxdepth(self, root:Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))
    
# Iterative DFS and BFS later
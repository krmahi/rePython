from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS
class solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # if left or right: root.left, root.right = root.right, root.left
        root.left, root.right = root.right,  root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
# iterative DFS
class solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return root
    
# BFS
class solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root
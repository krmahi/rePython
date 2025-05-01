from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right

class solution:
    def levelordertraversal(self, root: Optional[TreeNode])-> list[list[int]]:
        if not root: return []
        
        q = deque([root])
        res = []

        while q:
            n = len(q)
            tmp = []
            for i in range(n):
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right:  q.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        
        return res
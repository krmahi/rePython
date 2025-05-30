from typing import Optional
class TreeNode:
    def __int__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def isSubtree(self, root:Optional[TreeNode], subRoot:Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p:Optional[TreeNode], q:Optional[TreeNode])-> bool:
        if not p and not q: return True
        if p and q and p.val == q.val: return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        return False
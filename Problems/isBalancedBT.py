from typing import Optional 
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node) -> tuple:
            if not root: return True, 0
            left_bool, left = dfs(node.left)
            right_bool, right = dfs(node.right)
            balanced = (left_bool and right_bool and abs(left - right) <= 1)
            return balanced, 1 + max(left, right)

        return dfs(root)[0]
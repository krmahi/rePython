from TreeNode import TreeNode

# recursion
def lowestCommonAncestor(self, root: TreeNode,  p: TreeNode, q: TreeNode)-> TreeNode:
    if not root or root == q or root == p:
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right: return root

    return left if left else right

#iteration
def lowestCommonAncestor(self, root: TreeNode,  p: TreeNode, q: TreeNode)-> TreeNode:
    while root:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: return root
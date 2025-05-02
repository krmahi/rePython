from TreeNode import TreeNode

#recursion
def GoodNode(self, root: TreeNode):
    def dfs(node, max_val):
        if not root: return 0
        good = 1 if node.val >= max_val else 0
        return good + dfs(node.left, max_val) + dfs(node.right, max_val)
    
    return dfs(root, root.val)

#iterative
def GoodNode(self, root: TreeNode):
    good = 0

    def dfs(node, max_val):
        if node.val >= max_val:
            max_val = node.val
            good += 1
        if node.left: dfs(node.left, max_val)
        if node.right: dfs(node.right, max_val)

    dfs(root, root.val)
    return good
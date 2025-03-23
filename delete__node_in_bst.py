from typing import Optional # to give python optional parameter to have multiple values

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right

class solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: #here optional[TreeNode] means it can be either None or a node
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else: # root.val == key
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # when we have 2 child
            curr = root.right
            while curr.left:
                curr = curr.left
            # curr -> minimum in right subtree
            root.val = curr.val
            # curr still remains in right subtree (duplicate) so we have to delete curr from right subtree
            root.right = self.deleteNode(root.right, curr.val)
        return root
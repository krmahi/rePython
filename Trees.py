class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data: # duplicate value
            return False
        
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True
            
    def find(self, data):
        if self.data == data:
            return data
        
        elif self.data > data:
            if self.left:
                return self.left.find(data)    
            else:
                return False
        
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
            
    def delete(self, data):
        if not self:
            return self
        
        if self.data > data:
            if self.left:
                self.left = self.left.delete(data)
        
        elif self.data < data:
            if self.right:
                self.right = self.right.delete(data)

        else: # root.data == data
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            
            # when both child exist
            curr = self.right
            while curr.left:
                curr = curr.left
            # curr has the min in right subtree
            self.data = curr.data
            # to delete the curr node
            self.right = self.right.delete(curr.data)
        return self

    def preorder(self):
        if self:
            print(self.data, end = " ")
            if self.left: self.left.preorder()
            if self.right: self.right.preorder()
    
    def inorder(self):
        if self:
            if self.left: self.left.inorder()
            print(self.data, end = " ")
            if self.right: self.right.inorder()
    
    def postorder(self):
        if self:
            if self.left: self.left.postorder()
            if self.right: self.right.postorder()
            print(self.data, end = " ")

my_tree = Tree(10)
my_tree.insert(12)
my_tree.insert(200)
my_tree.insert(12)
my_tree.insert(18)
print(my_tree.find(2))
print(my_tree.find(5))
print(my_tree.find(10))
my_tree.delete(3)
my_tree.delete(12)
# my_tree.delete(4)
# my_tree.delete(5)
my_tree.preorder()
print()
my_tree.inorder()
print()
my_tree.postorder()
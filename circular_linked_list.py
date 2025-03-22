from Linked_node import Node

class circularLinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next = self.root
        else:
            new_node = Node(data, self.root.next)
            self.root.next = new_node
        self.size += 1

    def find(self, data):
        node = self.root
        while True:
            if node.data == data:
                return data
            elif node.next == self.root:
                return False
            node = node.next
    
    def remove(self, data):
        node = self.root
        prev_node = None
        while True:
            if node.data == data:
                if prev_node is not None:
                    prev_node.next = node.next
                else:
                    while not node.next == self.root:
                        node = node.next
                    # node is at the end
                    node.next = self.root.next
                    self.root = self.root.next
                self.size -= 1 
                return True
            elif node.next == self.root:
                return False
            prev_node = node
            node = node.next

    def print_list(self):
        if self.root == None:
            return
        node = self.root
        print(node, end="->")
        while not node.next == self.root:
            node = node.next
            print(node, end="->")
        print()

my_list = circularLinkedList()
for i in [1,2,3,4,5,6,7,8,9,10]:
    my_list.add(i)
my_list.print_list()
print(my_list.size)
print(my_list.find(3))
print(my_list.find(12))
my_list.remove(10)
my_list.print_list()
print(my_list.size)

#printing without print__list function

node = my_list.root
print(node, end="->")
for i in range(10): # to see if it actually circle back
    node = node.next
    print(node, end="->")
print()
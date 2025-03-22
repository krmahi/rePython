from Linked_node import Node

class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    
    def find(self, data):
        node = self.root
        while node is not None:
            if node.data == data:
                return data
            else:
                node = node.next
        return None
    
    def remove(self, data):
        node = self.root
        prev_node = None
        while node is not None:
            if node.data == data:
                if prev_node is not None: # none.next is nothing
                    prev_node.next = node.next
                else: self.root = node.next # on the root node
                self.size -= 1
                return True
            else:
                prev_node = node
                node = node.next
        return False
    
    def print_list(self):
        node = self.root
        while node is not None:
            print(node, end = "->")
            node = node.next
        print('None')

my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.print_list()
my_list.remove(2)
my_list.remove(1)
my_list.print_list()
print(my_list.find(1))
print(my_list.size)
print(type(my_list))
print(my_list.root)


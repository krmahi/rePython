from Linked_node import Node

class Doublylinkedlist:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    
    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
        else:
            new_node = Node(data, self.root)
            self.root.prev = new_node
            self.root = new_node
        self.size += 1

    def find(self, data):
        node = self.root
        while node:
            if node.data == data:
                return data
            else:
                node = node.next
        return False
    
    def remove(self, data):
        node = self.root
        prev_node = None
        while node:
            if node.data == data:
                if not node.next:
                    prev_node.next = None
                elif prev_node:
                    prev_node.next = node.next
                    node.next.prev = prev_node
                else:
                    self.root = self.root.next
                    self.root.prev = None
                self.size -= 1
                return True  
            else:
                prev_node = node
                node = node.next
        return False
    
    def print_list(self):
        node = self.root
        while node:
            print(node, end="->")
            node = node.next
        print()

my_list = Doublylinkedlist()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(6)
my_list.add(7)
my_list.add(8)
print(my_list.size)
my_list.print_list()
print(my_list.find(4))
print(my_list.find(10))
my_list.remove(5)
my_list.remove(6)
my_list.print_list()
print(my_list.size)
print(type(my_list))

my_list2 = Doublylinkedlist()
for i in range(10):
    my_list2.add(i)
my_list2.print_list()

print(my_list2.root.next.next.prev)
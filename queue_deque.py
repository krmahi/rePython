from collections import deque

# in python we use deque (double ended queue) for single queue
# append() -> enque || popleft() -> deque

my_queue = deque() # intialize queue using deque
my_queue.append(8)
my_queue.append('c')
my_queue.append([8,9])
print(my_queue)
print(my_queue.popleft())
print(my_queue.popleft())
print(my_queue.popleft())
print(my_queue)

# queue using a wrapper class

class queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def __str__(self):
        return str(self.queue)

my_queue_2 = queue()
my_queue_2.push(7)
my_queue_2.push(1)
my_queue_2.push([1,'c',3])
print(my_queue_2) # deque([7, 1, [1,'c',3]]) 
my_queue_2.pop()
my_queue_2.pop()
my_queue_2.pop()
print(my_queue_2) # deque([])
print(type(my_queue_2)) # queue


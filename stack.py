my_stack = list()
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)
my_stack.pop() # pop 5
print(my_stack.pop()) # pop 4 and print 4
print(my_stack) # 1, 2, 3

# wrapper class for stack
class Stack:
    def __init__(self): #constructor
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    
    def peek(self): # does not delete the top item
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    
    def __str__(self): # takes obj name
        return str(self.stack)
    

wrapper__stack = Stack() # initialize list()
wrapper__stack.push(7)
wrapper__stack.push(8)
wrapper__stack.push(9)
wrapper__stack.push(10)
wrapper__stack.push(5)
wrapper__stack.push('c')
print(wrapper__stack) # [7, 8, 9, 10, 5, 'c']
wrapper__stack.pop()
wrapper__stack.pop()
wrapper__stack.pop()
print(wrapper__stack) # [7, 8 ,9]
print(wrapper__stack.peek(), end = " ")
print(wrapper__stack.peek())
print(wrapper__stack) # [7, 8 ,9]
print(type(wrapper__stack)) # stack

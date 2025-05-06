# min operation cost time complexity O(n)
class minStack:
    def __init__(self):
        self.stack = list()
    
    def push(self, val:int):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def min_e(self):
        return min(self.stack)
    
# time complexity for every operation: O(1)
class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val:int):
        self.stack.append(val)
        if self.minStack: val = min(val, self.minStack[-1])
        self.minStack.append(val)
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def min_e(self):
        return self.minStack[-1]

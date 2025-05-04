class minStack:
    def __init__(self):
        self.stack = list()
    
    def push(self, val:int):
        self.stack.append(val)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def min_e(self):
        return min(self.stack)
    
        

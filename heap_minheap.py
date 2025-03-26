# complexities
# insert -> O(log n)
# get min -> O(1)
# remove/pop min -> O(log n)

# implemented using a list

# accessing relations
# i => heap indices (indexing can start from 1)
# parent (i) -> i // 2
# left (i) -> i * 2 (left child of i)
# right (i) -> i * 2 + 1 (right child of i)

# push() -> added (appended to the end of the list then compare with parents to get to the desired position)
# peek() -> return heap[1]
# pop() -> swap min (first) and last item in the list delete last item and store in min, now move down the swapped item to its position
#          ** compare with the min(left, right) child

class heap:
    def __init__(self, items = []):
        self.heap = [0]
        for item in items:
            self.push(item)

    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)
    def peek(self):
        return self.heap[1]
    
    def pop(self):
        if len(self.heap) == 2:
            min = self.heap.pop()
        elif len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            min = self.heap.pop()
            self.__bubbleDown(1)
        else: return None
        return min

    def __swap(self, i , j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def __floatUp(self, index):
        if index <= 1:
            return
        parent = index // 2
        if self.heap[parent] > self.heap[index]:
            self.__swap(parent, index)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        minimum = index
        if len(self.heap) > left and self.heap[minimum] > self.heap[left]:
            minimum = left
        if len(self.heap) > right and self.heap[minimum] > self.heap[right]:
            minimum = right
        if not minimum == index:
            self.__swap(minimum, index)
            self.__bubbleDown(minimum)
    
    def __str__(self):
        return str(self.heap)

my_heap = heap([2,10])
my_heap.push(1)
# my_heap.push(0)
print(my_heap)
print(my_heap.peek())
print(my_heap.pop())
print(my_heap)
print(type(my_heap))
print(my_heap.pop())
print(my_heap.pop())


    
# complexities
# insert -> O(log n)
# get max -> O(1)
# remove/pop max -> O(log n)

# implemented using a list

# accessing relations
# i => heap indices (indexing can start from 1)
# parent (i) -> i / 2
# left (i) -> i * 2 (left child of i)
# right (i) -> i * 2 + 1 (right child of i)

# push() -> added (appended to the end of the list then compare with parents to get to the desired position)
# peek() -> return heap[1]
# pop() -> swap max (first) and last item in the list delete last item and store in max, now move down the swapped item to its position
#          ** compare with the max(left, right) child
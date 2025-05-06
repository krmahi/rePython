from collections import deque

class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

# queue -> Time: O(n) space: O(n)
class solution:
    def Reorder(self, head: ListNode) -> None:
        if not head or not head.next: return

        queue = deque()
        curr = head.next

        while curr:
            queue.append(curr)
            curr = curr.next
        
        curr = head
        toggle = True
        
        while queue:
            if toggle: curr.next = queue.pop()
            else: curr.next = queue.popleft()
            toggle = False
            curr = curr.next
        
        curr.next = None

# Two pointers (slow and fast) to find mid: TIme -> O(n), space -> O(1)
class solution:
    def Reorder(self, head: ListNode) -> None:
        if not head or not head.next: return

        # Divide
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # reorder
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
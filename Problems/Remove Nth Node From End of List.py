class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# two pass: time -> O(n)
class solution:
    def RemoveNthNodeFromEndofList(self, head, n):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        if n == length: return head.next

        curr = head
        for _ in range(length - n - 1): curr = curr.next

        curr.next = curr.next.next

        return head
    
# one pass using two pointers (slow and fast and maintaning the n distance b/w them)
class solution:
    def RemoveNthNodeFromEndofList(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next
        # diff b/w slow and fast is n

        while fast:
            fast = fast.next
            slow = slow.next
        # now slow is always gonna be at a prev node to n

        slow.next = slow.next.next
        return dummy.next

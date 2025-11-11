from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None or head.next is None:
            return None
        if head.next.next is None:
            return head.val + head.next.val
        
        # find middle node
        middle = head
        end = head.next

        while end.next:
            middle = middle.next
            end = end.next.next

        # reverse second half nodes
        current = middle.next
        middle.next = None
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # calculate pair sum
        current = head
        result = []
        while current and end:
            result.append(current.val + end.val)
            current = current.next
            end = end.next
        
        # return max pair sum
        return max(result)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        current_node = head
        while current_node.next is not None:
            nodes.append(ListNode(val=current_node.val, next=None))
            current_node = current_node.next
        nodes.append(ListNode(val=current_node.val, next=None))

        nodes.pop(int(len(nodes)/2))

        if len(nodes) == 1:
            return nodes[0]
        if len(nodes) == 0:
            return None
        for idx in range(len(nodes)-1):
            nodes[idx].next = nodes[idx+1]
        return nodes[0]
        
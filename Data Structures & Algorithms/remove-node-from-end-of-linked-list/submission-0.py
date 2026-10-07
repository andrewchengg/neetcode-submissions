# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        if len(nodes) == 1: 
            head.next = None
            head = head.next
            return head
        to_remove = nodes[len(nodes) - n] #target node
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head 
        while curr:
            nxt = curr.next
            if curr == to_remove:
                prev.next = nxt
            prev = curr #shifts prev forward
            curr = curr.next #shifts curr forward
        return dummy.next

                
                


#removing the nth node from the end of the list, not starting from the front 
        
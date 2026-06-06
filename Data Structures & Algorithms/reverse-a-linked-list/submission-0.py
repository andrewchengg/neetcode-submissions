# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nxt = None
        prev = None 
        while curr:
            nxt = curr.next #defines what next is 
            curr.next = prev #gets the next element to point to current
            prev = curr
            curr = nxt
        return prev
        
       
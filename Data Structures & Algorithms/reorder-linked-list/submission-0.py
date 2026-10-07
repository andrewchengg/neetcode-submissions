# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        lst = [] 
        while curr:
            lst.append(curr) #storing a list of nodes 
            curr = curr.next
        curr = head
        switch = False
        left = 1
        right = len(lst) - 1 
        for i in range(len(lst) - 1):
            if not switch:
                curr.next = lst[right]
                right -= 1
                switch = True
                curr = curr.next
            elif switch:
                curr.next = lst[left]
                left += 1 
                switch = False
                curr = curr.next
        curr.next = None

             
            
            
        
            
            
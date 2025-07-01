# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None , head
        while curr:
            temp = curr.next #Store next one
            curr.next = prev #Reverse Pointer
            prev = curr # Store prev
            curr = temp # Move to Next
        return prev

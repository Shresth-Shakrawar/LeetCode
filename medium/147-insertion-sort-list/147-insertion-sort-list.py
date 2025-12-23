            nextNode = curr.next
        while curr != None:
        dummy = ListNode(0,next=None)
        curr = head
        if head == None or head.next == None:
            return head
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         self.next = next
#         self.val = val
#     def __init__(self, val=0, next=None):
# class ListNode:
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        currNext = curr.next
        prevNode = None

        while currNext:
            curr.next = prevNode
            prevNode = curr
            curr = currNext
            currNext = currNext.next
        
        curr.next = prevNode
            
        return curr
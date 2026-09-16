# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        nth = size - n
        if nth == 0:
            return head.next

        curr = head
        while nth > 1:
            nth -= 1
            curr = curr.next
        
        toRemove = curr.next
        curr.next = toRemove.next if toRemove else None

        return head
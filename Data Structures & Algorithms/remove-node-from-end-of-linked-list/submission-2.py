# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the size
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        # Find the inverse for n
        toRemoveN = size - n

        # Remove toRemoveN
        toRemove = head
        prev = None
        while toRemoveN > 0:
            toRemoveN -= 1
            prev = toRemove
            toRemove = toRemove.next

        nextNode = toRemove.next
        if prev:
            prev.next = nextNode
        else:
            return nextNode

        return head

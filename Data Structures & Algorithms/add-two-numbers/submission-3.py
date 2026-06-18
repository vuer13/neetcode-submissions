# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        num = 0

        val1 = l1.val
        val2 = l2.val
        
        head = ListNode(val1 + val2, None)
        curr = head

        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            totalVal = val1 + val2
            if curr.val > 9:
                curr.val = curr.val % 10
                totalVal += 1
            
            newNode = ListNode(totalVal, None)
            curr.next = newNode

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        print(l1)
        print(l2)
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        if curr.val > 9:
            curr.val = curr.val % 10
            newNode = ListNode(1, None)
            curr.next = newNode
            curr = curr.next

        return head
            
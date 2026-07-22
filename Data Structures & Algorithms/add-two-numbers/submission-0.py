# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        s1 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        s2 = ''
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        # Reverse because digits are stored in reverse order
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])

        total = str(num1 + num2)

        # Reverse result because output also needs reverse order
        total = total[::-1]

        dummy = ListNode()
        tail = dummy

        for digit in total:
            new_node = ListNode(int(digit))
            tail.next = new_node
            tail = tail.next

        return dummy.next
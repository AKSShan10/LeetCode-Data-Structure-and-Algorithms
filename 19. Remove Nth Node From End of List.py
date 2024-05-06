# dummy = ListNode(0)
# size = 0
# curr = head
# while curr:
#     curr = head.next
#     size += 1
#
# if (size == n):
#     return head.next
#
# pts = size - 1
# p = 1
# prev = head
# while (p < pts):
#     prev = head.next
#     p += 1
#
# prev.next = prev.next.next
# return dummy.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        right = dummy
        left = dummy
        for _ in range(n + 1):
            right = right.next

        while right is not None:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


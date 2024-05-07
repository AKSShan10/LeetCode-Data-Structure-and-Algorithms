# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def findMiddle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return True
        fhe = self.findMiddle(head)
        shs = self.reverse(fhe.next)
        fhs = head
        while shs:
            if fhs.val != shs.val:
                return False
            fhs = fhs.next
            shs = shs.next
        return True

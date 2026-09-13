# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 迭代法反转后半段链表
        prev = None
        curr = slow
        while curr:
            new_temp = curr.next
            curr.next = prev
            prev = curr
            curr = new_temp
        # 前后一起比较
        pa = head
        pb = prev
        while pb:
            if pa.val != pb.val:
                return False
            pa = pa.next
            pb = pb.next
        return True
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            # 三步交换
            first.next = second.next
            second.next = first
            prev.next = second
            # 向下一组移动
            prev = first
        return dummy.next
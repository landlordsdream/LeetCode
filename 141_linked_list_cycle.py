# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # 快慢指针
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
        
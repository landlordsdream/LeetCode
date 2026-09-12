# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

# 交换法 pa pb 均遍历两链表
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
    
# 链表长度差值法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        lenA = 0
        lenB = 0
        while pa:
            lenA += 1
            pa = pa.next
        while pb:
            lenB += 1
            pb = pb.next
        pa = headA
        pb = headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                pa = pa.next
        else:
            for _ in range(lenB - lenA):
                pb = pb.next
        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return pa
        
        
        

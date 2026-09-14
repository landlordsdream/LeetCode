# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 变量carry 保存
        # digit 当前位数字
        # total = l1.val + l2.val + carry
        # carry = total // 10
        # digit = total % 10
        
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        # 只要l1 l2 carry 其中一个没有走完就继续
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10
            
            curr.next = ListNode(digit)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next






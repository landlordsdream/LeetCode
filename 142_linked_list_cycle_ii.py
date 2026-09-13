# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # x 头节点到环入口的距离
        # y 环入口到相遇点A的距离
        # z 相遇点到环入口的距离
        
        # 因为快指针是慢指针速度2倍 2*(x+y) = x+y + n*(y+z)
        # x = z + (n-1)*(y+z) 后者是圈数
        # 所以可以构建 时间等于步长   找到环入口
        
        # 快慢指针
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast

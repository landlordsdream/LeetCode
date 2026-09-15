# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 哑节点，简化头结点处理
        dummy = ListNode(-1)
        dummy.next = head
        # group_prev 当前组的前一个节点
        group_prev = dummy
        
        while True:
            # 从group_prev节点找下一组第k个节点kth
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    break
            # 不够k个 结束 因为前一轮已经接上后续节点 后面会交代
            if kth is None:
                break
            
            # 记录关键节点 这一组第一个节点和下一组第一个节点
            first = group_prev.next
            new_first = kth.next
            
            # 翻转first~kth之间k个节点
            prev = None
            curr = first
            count = 0
            while curr and count < k:
                new_temp = curr.next
                curr.next = prev
                prev = curr
                curr = new_temp
                count += 1
            
            # 连接链表
            # 前一组接这一组头结点 这一组末尾接下一组起始节点
            group_prev.next = prev
            first.next = new_first
            # 移到这一组末尾 准备下一组
            group_prev = first
        return dummy.next
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # 哈希表
        mapping = {}
        curr = head
        # 复制所有节点 存映射
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_curr = mapping[curr]
            new_curr.next = mapping[curr.next] if curr.next else None
            new_curr.random = mapping[curr.random] if curr.random else None
            curr = curr.next
        return mapping[head]


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # 复制 + 拆分
        curr = head
        while curr:
            new_Node = Node(curr.val)
            new_Node.next = curr.next
            curr.next = new_Nodegit 
            curr = new_Node.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        dummy = Node(-1)
        new_curr = dummy
        curr = head
        while curr:
            new_curr.next = curr.next  # dummy->A'
            new_curr = new_curr.next  # A'
            curr.next = curr.next.next  # 跳过A'
            curr = curr.next  # A -> B
        return dummy.next




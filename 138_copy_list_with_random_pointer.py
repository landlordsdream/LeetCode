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





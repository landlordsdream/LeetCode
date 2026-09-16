# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# 第一思路是比较 然后是分治 虽然分治思路还不太明 分 快慢指针找到中段然后呢 再分分到最小单位 然后用之前合并两个有序链表 不断重复 可是分开后就好多份像什么来着 对坚信分开后的链表会像函数本身一样可以排序
		# 好吧递归
		if head is None or head.next is None:
			return head
		fast = head
		slow = head
		# 判断条件 因为fast一次移动两步 不论链表奇偶都能保证和slow在链表中间
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		# 模拟链表被分为两个链表
		dummy = ListNode(-1)
		first = head
		second = slow.next
		slow.next = None
		L1 = self.sortList(first)
		L2 = self.sortList(second)
		curr = dummy
		curr1 = L1
		curr2 = L2
		while curr1 and curr2:
			if curr1.val < curr2.val:
				curr.next = curr1
				curr1 = curr1.next
				curr = curr.next
			else:
				curr.next = curr2
				curr2 = curr2.next
				curr = curr.next
		if curr1 is None:
			curr.next = curr2
		if curr2 is None:
			curr.next = curr1
		return dummy.next


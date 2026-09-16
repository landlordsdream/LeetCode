# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        #  merge an array of K sorted lists
        # 边界问题 只处理 None [] 空值和空列表 [[]] = [None] 包好一个空值的列表或者说一个空链表不在这处理
        if not lists:
            return None
        
        first_list = lists[0]
        curr1 = first_list
        
        for i in range(1, len(lists)):
            dummy = ListNode(-1)
            curr = dummy
            second_list = lists[i]
            curr2 = second_list
            
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
            else:
                curr.next = curr1
                
            first_list = dummy.next
            curr1 = first_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # 链表数组
        if not lists:
            return None
        
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(-1)
            curr = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next
        
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]

        
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            b = head.next
            b.next = head
            b.next.next = None
            return b
        if head.next.next.next is None:
            a = head
            b = a.next
            c = b.next
            b.next = a
            a.next = c
            return b
        current = ListNode(0,head)
        new_head = current
        while current is not None:
            if current.next is None:
                break
            if current.next.next is None:
                break
            x = current
            a = current.next
            b = current.next.next
            c = current.next.next.next
            x.next = b
            b.next = a
            a.next = c
            current = a
        return new_head.next

    def _list_to_node(self, _list: List[int]) -> Optional[ListNode]:
        if len(_list) == 0:
            return None
        start = ListNode(_list[0])
        current = start
        for i in range(1, len(_list)):
            current.next = ListNode(_list[i])
            current = current.next
        return start

if __name__ == '__main__':
    s = Solution()
    n = s._list_to_node([1,2])
    s.swapPairs(n)
    n = s._list_to_node([1,2,3])
    s.swapPairs(n)
    n = s._list_to_node([1,2,3,4])
    s.swapPairs(n)
    n = s._list_to_node([1,2,3,4,5])
    s.swapPairs(n)
    n = s._list_to_node([1,2,3,4,5,6])
    s.swapPairs(n)
    n = s._list_to_node([1,2,3,4,5,6,7])
    s.swapPairs(n)


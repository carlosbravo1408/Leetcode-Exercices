# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def _list_to_node(self, _list: List[int]) -> Optional[ListNode]:
        if len(_list) == 0:
            return None
        start = ListNode(_list[0])
        current = start
        for i in range(1, len(_list)):
            current.next = ListNode(_list[i])
            current = current.next
        return start

    def _node_to_list(self, node: Optional[ListNode]) -> List[int]:
        if node is None:
            return []
        data = list()
        current = node
        while current:
            data.append(current.val)
            current = current.next
        return data

    #lazy approach
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if k == 1:
            return head
        _list = self._node_to_list(head)
        if len(_list) < k:
            return head
        if len(_list) == k:
            return self._list_to_node(_list[::-1])
        left, right = 0, k
        while left < len(_list) and right <= len(_list):
            _list[left: right] = _list[left:right][::-1]
            left += k
            right += k
        return self._list_to_node(_list)


if __name__ == '__main__':
    s = Solution()
    n = s._list_to_node([1, 2])
    s.reverseKGroup(n, 1)
    n = s._list_to_node([1, 2, 3])
    s.reverseKGroup(n, 2)
    n = s._list_to_node([1, 2, 3, 4])
    s.reverseKGroup(n, 3)
    n = s._list_to_node([1, 2, 3, 4, 5])
    s.reverseKGroup(n, 2)
    n = s._list_to_node([1, 2, 3, 4, 5, 6])
    s.reverseKGroup(n, 3)
    n = s._list_to_node([1, 2, 3, 4, 5, 6, 7])
    s.reverseKGroup(n, 4)
    n = s._list_to_node([1, 2, 3, 4, 5])
    s.reverseKGroup(n, 3)

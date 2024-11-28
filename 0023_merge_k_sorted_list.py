# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional


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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l is not None]
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        v = []
        for l in lists:
            if l is not None:
                v+=self._node_to_list(l)
        if len(v) == 0:
            return None
        return self._list_to_node(sorted(v))

if __name__ == '__main__':
    s = Solution()
    s.mergeKLists([None, None, None])
    s.mergeKLists([None, None, None, s._list_to_node([1, 2, 4])])
    s.mergeKLists([None, None, None, s._list_to_node([1, 2, 4]), None, s._list_to_node([1, 3, 4])])
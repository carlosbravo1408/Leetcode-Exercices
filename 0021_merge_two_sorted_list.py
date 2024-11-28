# https://leetcode.com/problems/merge-two-sorted-lists/description/
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

    # lazy approach
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[
        ListNode]) -> Optional[ListNode]:
        return self._list_to_node(
            sorted(
                self._node_to_list(list1)+self._node_to_list(list2)
            )
        )

    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[
        ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        current1 = list1
        current2 = list2
        if current1.val <= current2.val:
            start = ListNode(current1.val)
            current1 = current1.next
        else:
            start = ListNode(current2.val)
            current2 = current2.next
        output = start
        while current1 or current2:
            v1 = current1.val if current1 else None
            v2 = current2.val if current2 else None
            if v1 is None:
                output.next = ListNode(current2.val)
                current2 = current2.next
            elif v2 is None:
                output.next = ListNode(current1.val)
                current1 = current1.next
            elif v1 <= v2:
                output.next = ListNode(current1.val)
                current1 = current1.next
            else:
                output.next = ListNode(current2.val)
                current2 = current2.next
            output = output.next
        return start


if __name__ == "__main__":
    s = Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    list1 = s._list_to_node(list1)
    list2 = s._list_to_node(list2)
    s.mergeTwoLists(list1, list2)
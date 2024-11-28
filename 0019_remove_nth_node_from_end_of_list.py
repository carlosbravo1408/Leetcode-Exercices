# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[
        ListNode]:
        depth = 1
        current = head
        while current.next is not None:
            depth += 1
            current = current.next
        steps = depth - n
        if depth == 1 and n == 1:
            return None
        if steps == 0:
            return head.next
        prev_node = head
        current = head
        for _ in range(steps):
            prev_node = current
            current = current.next
        prev_node.next = current.next
        return head


def convert_list_to_node_list(data: List[int]) -> Optional[ListNode]:
    current_node = ListNode(data[0])
    first_node = current_node
    for i in data[1:]:
        current_node.next = ListNode(i)
        current_node = current_node.next
    return first_node


if __name__ == '__main__':
    s = Solution()
    s.removeNthFromEnd(head=convert_list_to_node_list([1, 2, 3, 4, 5]),
                       n=2)  # expected [1,2,3,5]
    s.removeNthFromEnd(head=convert_list_to_node_list([1]), n=1)  # expected []
    s.removeNthFromEnd(head=convert_list_to_node_list([1, 2]),
                       n=1)  # expected [1]
    s.removeNthFromEnd(head=convert_list_to_node_list([1, 2]),
                       n=2)  # expected [2]

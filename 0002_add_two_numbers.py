# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        aux_result = None
        current_l1 = l1
        current_l2 = l2
        carry = 0
        while True:
            adder = current_l1.val + current_l2.val + carry
            carry = 1 if adder > 9 else 0
            if result is None:
                aux_result = ListNode(adder % 10)
                result = aux_result
            else:
                result.next = ListNode(adder % 10)
                result = result.next
            if current_l1.next is None and current_l2.next is None:
                if carry > 0:
                    result.next = ListNode(carry)
                return aux_result
            current_l1 = current_l1.next if current_l1.next is not None else ListNode()
            current_l2 = current_l2.next if current_l2.next is not None else ListNode()
        return aux_result

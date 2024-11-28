# https://leetcode.com/problems/generate-parentheses/
from typing import List, Optional

V = {-1: "(", 1:")"}
class BinaryNode:
    def __init__(self, val=1, parent:Optional['BinaryNode']=None):
        self.val = val
        self.parent = parent
        self.carry = self.val + (self.parent.carry if parent else 0)
        self.open = (self.val > 0) + ((self.parent.open) if parent else 0)

    def str(self):
        current = self
        result = ''
        while current:
            result += V[current.val]
            current = current.parent
        return result

class Solution:
    def generate_leaf(self, node: BinaryNode, n: int, result: list):
        if node.open<n:
            self.generate_leaf(BinaryNode(1, node), n, result)
        if node.carry>0:
            self.generate_leaf(BinaryNode(-1, node), n, result)
        if node.open == n and node.carry == 0:
            result.append(node.str())

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        leafs = []
        self.generate_leaf(BinaryNode(1), n, leafs)
        return leafs

if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(2)
    s.generateParenthesis(3)

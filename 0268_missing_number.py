# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        data = set(nums)
        for i in range(len(nums)+1):
            if i not in data:
                return i
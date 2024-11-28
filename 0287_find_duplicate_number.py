# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        data = set()
        for num in nums:
            if num in data:
                return num
            data.add(num)


if __name__ == "__main__":
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2

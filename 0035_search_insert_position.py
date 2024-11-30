# https://leetcode.com/problems/search-insert-position/description/
from typing import List


class Solution:
    def binary_search(
            self,
            nums: List[int],
            target: int,
            start:int=0,
            end:int=None
    ) -> int:
        if len(nums) == 0:
            return 0
        if end == None:
            end = len(nums) - 1
        if start < 0 or end >= len(nums):
            return 0
        if end == start:
            if end == len(nums) - 1 and target > nums[end]:
                return len(nums)
            return start
        pivot = start + (end - start) // 2
        while True:
            if target == nums[pivot]:
                return pivot
            if target < nums[pivot]:
                return self.binary_search(nums, target, start, pivot)
            else:
                return self.binary_search(nums, target, pivot+1, end)

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = self.binary_search(nums, target, 0, len(nums)-1)
        return n

if __name__ == '__main__':
    sol = Solution()
    assert sol.searchInsert([1,3,5,6], 5) == 2
    assert sol.searchInsert([1,3,5,6], 2) == 1
    assert sol.searchInsert([1,3,5,6], 7) == 4
    assert sol.searchInsert([1], 2) == 1
    assert sol.searchInsert([1], 0) == 0
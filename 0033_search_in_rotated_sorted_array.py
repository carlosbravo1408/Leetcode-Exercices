# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
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
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if end == None:
            end = len(nums) - 1
        if start < 0 or end >= len(nums):
            return -1
        if end - start == 0:
            return start if nums[start] == target else -1
        pivot = start + (end - start) // 2
        while True:
            if target == nums[pivot]:
                return pivot
            if target < nums[pivot]:
                return self.binary_search(nums, target, start, pivot)
            else:
                return self.binary_search(nums, target, pivot+1, end)

    def _find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return 0
        while left <= right:
            mid = (left + right) // 2
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search1(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        pivot = self._find_pivot(nums)
        if nums[pivot] == target:
            return pivot
        elif nums[0] <= target <= nums[pivot]:
            return self.binary_search(nums, target, 0, pivot)
        else:
            return self.binary_search(nums, target, pivot+1, len(nums)-1)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return self.binary_search(nums, target, 0, len(nums) - 1)
        while left <= right:
            pivot = (left + right) // 2
            if pivot < len(nums) - 1 and nums[pivot] > nums[pivot + 1]:
                if nums[pivot] == target:
                    return pivot
                elif nums[0] <= target <= nums[pivot]:
                    return self.binary_search(nums, target, 0, pivot)
                else:
                    return self.binary_search(nums, target, pivot + 1, len(nums) - 1)
            elif nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search( [4,5,6,7,0,1,2], 0))
    print(sol.search( [4,5,6,7,0,1,2], 3))
    print(sol.search( [1], 0))
    print(sol.search( [1,3], 0))
    print(sol.search( [1,3], 3))
    print(sol.search( [3,5,1], 3))
    print(sol.search( [3,4,5,6,1,2], 2))
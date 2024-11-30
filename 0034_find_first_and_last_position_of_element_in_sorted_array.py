# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
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

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        val = self.binary_search(nums, target)
        result = [-1, -1]
        if val != -1:
            l, r = val, val
            l_l, l_r = False, False
            while l>=0 or r < len(nums):
                if l_l and l_r:
                    break
                if not l_l and nums[l] == nums[val]:
                    result[0] = l
                    l -= 1
                if l<0 or nums[l] != nums[val]:
                    l_l = True
                if not l_r and nums[val] == nums[r]:
                    result[1] = r
                    r += 1
                if r>=len(nums) or nums[r] != nums[val]:
                    l_r = True
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([1], 1))
    print(sol.searchRange([2,2], 3))
    print(sol.searchRange([2,2], 2))
    print(sol.searchRange([2,2], 2))
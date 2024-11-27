# https://leetcode.com/problems/median-of-two-sorted-arrays/
from statistics import median
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))

if __name__ == '__main__':
    assert 2.0 == Solution().findMedianSortedArrays([1,3],[2])
    assert 2.5 == Solution().findMedianSortedArrays([1,2],[3,4])
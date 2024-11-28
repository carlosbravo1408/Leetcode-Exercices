# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        data = set(nums)
        nums[0:len(data)] = sorted(list(data))
        return len(data)

if __name__ == '__main__':
    s = Solution()
    assert s.removeDuplicates([1,1,2]) == 2
    assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
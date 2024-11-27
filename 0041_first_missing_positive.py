# https://leetcode.com/problems/first-missing-positive/
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for num in range(len(nums)+1):
            if num+1 not in nums:
                return num+1

if __name__ == '__main__':
    assert Solution().firstMissingPositive([1])==2
    assert Solution().firstMissingPositive([1,2,0])==3
    assert Solution().firstMissingPositive([3,4,-1,1])==2
    assert Solution().firstMissingPositive([7,8,9,11,12])==1
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        data = {}
        for i, value in enumerate(nums):
            if target - value in data:
                return i, data[target - value]
            data[value] = i

if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [0, 1]
    assert Solution().twoSum([3, 3], 6) == [0, 1]

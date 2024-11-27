from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        data = set()
        for num in nums:
            if num not in data:
                data.add(num)
            elif num in data:
                data.remove(num)
        return list(data)

if __name__ == '__main__':
    assert Solution().singleNumber([1,2,1,3,2,5]) == [3,5]
    assert Solution().singleNumber([-1, 0]) == [-1, 0]
    assert Solution().singleNumber([0, 1]) == [0, 1]
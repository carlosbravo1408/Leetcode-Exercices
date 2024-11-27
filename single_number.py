from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        data = set()
        for i in nums:
            if i not in data:
                data.add(i)
            elif i in data:
                data.remove(i)
        return data.pop()

if __name__ == '__main__':
    assert Solution().singleNumber([2,2,1]) == 1
    assert Solution().singleNumber([4,1,2,1,2]) == 4
    assert Solution().singleNumber([1]) == 1
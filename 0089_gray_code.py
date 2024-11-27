# https://leetcode.com/problems/gray-code/
from typing import List


class Solution:
    def _int32_to_gray(self, n: int) -> int:
        n = n ^ n >> 1
        n ^= n >> 2
        n ^= n >> 4
        n ^= n >> 8
        n ^= n >> 16
        return n

    def grayCode(self, n: int) -> List[int]:
        return [_n ^ _n >> 1 for _n in range(1<<n)]

if __name__ == '__main__':
    assert Solution().grayCode(2) == [0, 1, 3, 2]
    assert Solution().grayCode(3) == [0,1,3,2,6,7,5,4]

# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        # n = n & 0xFFFFFFFF
        n = ((n >> 16) | (n << 16)) & 0xFFFFFFFF
        n = (((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)) & 0xFFFFFFFF
        n = (((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)) & 0xFFFFFFFF
        n = (((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)) & 0xFFFFFFFF
        n = (((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)) & 0xFFFFFFFF
        return n


if __name__ == '__main__':
    assert Solution().reverseBits(
        0b00000010100101000001111010011100) == 964176192
    assert Solution().reverseBits(
        0b11111111111111111111111111111101) == 3221225471

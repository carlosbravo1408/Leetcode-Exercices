from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return bits[i] == 0b0
            elif i == len(bits) - 2:
                return bits[i]<<1|bits[i+1] == 0b0
            elif bits[i]<<1|bits[i+1] != 1:
                i = i + 2
            else:
                i += 1
        return False

if __name__ == '__main__':
    assert Solution().isOneBitCharacter([1, 0, 0])
    assert not Solution().isOneBitCharacter([1, 1, 1, 0])
    assert Solution().isOneBitCharacter([1, 1, 0, 0])

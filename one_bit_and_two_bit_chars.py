from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        valid_chars = (0b10, 0b11, 0b0)
        last_char = 0b0
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return bits[i] == last_char
            elif i == len(bits) - 2:
                return bits[i]<<1|bits[i+1] == last_char
            elif bits[i]<<1|bits[i+1] in valid_chars:
                i = i + 2
            elif bits[i]<<1|bits[i+1]:
                i += 1
        return False

if __name__ == '__main__':
    assert Solution().isOneBitCharacter([1, 0, 0])
    assert not Solution().isOneBitCharacter([1, 1, 1, 0])
    assert Solution().isOneBitCharacter([1, 1, 0, 0])

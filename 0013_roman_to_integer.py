# https://leetcode.com/problems/roman-to-integer/
class Solution:
    VALUES = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        prev_c = s[0]
        total = 0
        for c in s:
            if self.VALUES[prev_c] < self.VALUES[c]:
                total -= 2 * self.VALUES[prev_c]
            total += self.VALUES[c]
            prev_c = c
        return total


if __name__ == '__main__':
    assert Solution().romanToInt('III') == 3
    assert Solution().romanToInt('LVIII') == 58
    assert Solution().romanToInt('MCMXCIV') == 1994

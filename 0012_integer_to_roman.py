# https://leetcode.com/problems/integer-to-roman/
class Solution:
    VALUES = {
        1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 0: ''
    }
    PATTERN = [[], [1], [1, 1], [1, 1, 1], [1, 5], [5], [5, 1], [5, 1, 1],
               [5, 1, 1, 1], [1, 10]]

    def intToRomanI(self, num: int) -> str:
        response = ''
        for v in self.PATTERN[num // 1000]:
            response += self.VALUES[v * 1000]
        num = num % 1000
        for v in self.PATTERN[num // 100]:
            response += self.VALUES[v * 100]
        num = num % 100
        for v in self.PATTERN[num // 10]:
            response += self.VALUES[v * 10]
        for v in self.PATTERN[num % 10]:
            response += self.VALUES[v]
        return response

    def intToRoman(self, num: int) -> str:
        response = ''
        for v in self.PATTERN[num // 1000]:
            response += self.VALUES[v * 1000]
        num = num % 1000
        for v in self.PATTERN[num // 100]:
            response += self.VALUES[v * 100]
        num = num % 100
        for v in self.PATTERN[num // 10]:
            response += self.VALUES[v * 10]
        num = num % 10
        for v in self.PATTERN[num // 1]:
            response += self.VALUES[v]
        return response


if __name__ == '__main__':
    assert Solution().intToRoman(3749) == 'MMMDCCXLIX'
    assert Solution().intToRoman(58) == 'LVIII'
    assert Solution().intToRoman(1994) == 'MCMXCIV'

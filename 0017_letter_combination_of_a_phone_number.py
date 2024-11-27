# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import itertools
from typing import List


class Solution:
    KEYBOARD = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = itertools.product(*[self.KEYBOARD[digit] for digit in digits])
        return [''.join(s) for s in result]

if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("2") == ["a","b","c"]
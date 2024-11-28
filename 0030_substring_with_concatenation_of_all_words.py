# https://leetcode.com/problems/substring-with-concatenation-of-all-words
from typing import List, Dict, Iterable


class CustomSet(set[int]):
    def __init__(self, seq: Iterable[int] = ()):
        super().__init__()
        self.__data: Dict[int, int] = {}
        self.__items_added = 0
        if seq is not None:
            for num in seq:
                self.add(num)

    def add(self, num: int) -> None:
        if num not in self.__data:
            self.__data[num] = 0
        self.__data[num] += 1
        self.__items_added += 1
        super().add(num)

    def occurrences(self, num: int) -> int:
        if num not in self:
            return 0
        return self.__data[num]

    @property
    def length(self) -> int:
        return self.__items_added


class Solution:
    def findSubstring(self, s, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        s_length = len(s)
        if all([words[0] == word for word in words]):
            words = [''.join(words)]
        word_length = len(words[0])
        max_permuted_word_length = word_length * len(words)
        if s_length < max_permuted_word_length:
            return []
        words = CustomSet(words)
        l, r = 0, 0
        result = []
        while l < s_length and l + max_permuted_word_length <= s_length:
            coincidences = CustomSet()
            r = l
            while r < len(s) and r + word_length <= s_length:
                slice_word = s[r:r + word_length]
                if slice_word in words and coincidences.occurrences(
                        slice_word) < words.occurrences(slice_word):
                    coincidences.add(slice_word)
                    r += word_length
                    if coincidences.length == words.length:
                        result.append(l)
                        break
                else:
                    break
            l += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sorted(
        sol.findSubstring(s="barfoothefoobarman", words=["foo", "bar"])) == [0, 9]
    assert sol.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]) == []
    assert sol.findSubstring(s="ababababab", words=["ababa", "babab"]) == [0]
    assert sol.findSubstring(s="fffffffffffffffffffffffffffffffff", words=["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == []
    assert sorted(sol.findSubstring(s="bcabbcaabbccacacbabccacaababcbb", words=["c", "b", "a", "c", "a", "a", "a", "b", "c"])) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

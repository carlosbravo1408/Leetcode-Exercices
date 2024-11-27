# https://leetcode.com/problems/regular-expression-matching/
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        t =  re.fullmatch(rf"\b{p}\b", s)
        return t is not None

if __name__ == '__main__':
    assert not Solution().isMatch("aa", "a")
    assert Solution().isMatch("aa", "a*")
    assert Solution().isMatch("ab", ".*")
    assert not Solution().isMatch("abcd", "d*")
    assert not Solution().isMatch("bbab", "b*a*")
    assert not Solution().isMatch("bbba", "a*")
    assert not Solution().isMatch("bb", "c*")
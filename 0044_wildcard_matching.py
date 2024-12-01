# https://leetcode.com/problems/wildcard-matching/
import re


class Solution:
    # Time limit exceeded with 10th testcase
    def isMatch1(self, s: str, p: str) -> bool:
        regex_pattern = "^" + re.sub(r'\*+', '.*', p.replace('?', '.')) + "$"
        regex = re.compile(regex_pattern)
        return bool(regex.match(s))

    # https://leetcode.com/problems/wildcard-matching/solutions/5690858/easy-o-n-solution-beats-99/
    def isMatch(self, s: str, p: str) -> bool:
        first, second = 0, 0
        length1, length2 = len(p), len(s)
        star_index, match_index = -1, -1

        while second < length2:
            if first < length1 and (p[first] == s[second] or p[first] == '?'):
                first += 1
                second += 1
            elif first < length1 and p[first] == '*':
                star_index = first
                match_index = second
                first += 1
            elif star_index != -1:
                first = star_index + 1
                match_index += 1
                second = match_index
            else:
                return False

        while first < length1 and p[first] == '*':
            first += 1

        return first == length1

if __name__ == '__main__':
    assert not Solution().isMatch("aa", "a")
    assert Solution().isMatch("aa", "*")
    assert not Solution().isMatch("cb", "?a")
    assert Solution().isMatch("adceb", "*a*b")
    assert not Solution().isMatch("acdcb", "a*c?b")
    assert not Solution().isMatch("aab", "c*a*b")
    assert Solution().isMatch("", "******")
    assert Solution().isMatch("", "")
    assert not Solution().isMatch("", "*a*")
    assert not Solution().isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb")

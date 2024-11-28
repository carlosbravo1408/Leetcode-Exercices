# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def srtSrt(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        l = 0
        if m == n:
            return 0 if haystack == needle else -1
        elif m < n:
            return -1
        while l < m and l + n <= m:
            if haystack[l] == needle[0]:
                if needle == haystack[l:l + n]:
                    return l
            l += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.srtSrt(haystack="hello", needle="ll") == 2
    assert s.srtSrt(haystack="sadbutsad", needle="sad") == 0
    assert s.srtSrt(haystack="leetcode", needle="leeto") == -1
    assert s.srtSrt(haystack="a", needle="a") == 0

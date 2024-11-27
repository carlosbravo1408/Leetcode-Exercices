# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def _validate_substring(self, substring) -> bool:
        return substring == substring[::-1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 0
        l_max, r_max = 0, 1
        i = 0
        while 1:
            if i >= len(s) - 1:
                break
            i += 1
            if i<len(s)-1 and s[i + 1] == s[i - 1]:
                l = i - 1
                if s[i] == s[i + 1]:
                    for j in range(i, len(s)):
                        if s[j] != s[i]:
                            break
                        r = j
                        i = r
                else:
                    r = i + 1
            elif i>0 and s[i] == s[i - 1]:
                l = i - 1
                r = i
            else:
                continue
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > max_len:
                        max_len = r-l+1
                        l_max = l
                        r_max = r + 1
                    l -= 1
                    r += 1
                else:
                    break
        return s[l_max:r_max]

if __name__ == '__main__':
    print(Solution().longestPalindrome('abab'))
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('ac'))
    print(Solution().longestPalindrome('bb'))
    print(Solution().longestPalindrome('aaaa'))
    print(Solution().longestPalindrome('aaaaa'))
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('bananas'))
    print(Solution().longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))

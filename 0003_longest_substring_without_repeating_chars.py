# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 0
        i = 0
        while i < len(s)-1:
            data = {s[i]}
            for j in range(i+1, len(s)):
                if s[j] in data:
                    break
                data.add(s[j])
            i = j
            max_len = len(data) if len(data) > max_len else max_len
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        l = 0
        max_len = 0
        count = {}
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while count[s[r]] > 1:
                count[s[l]] = count[s[l]] - 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len




if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("dvdf"))
    print(Solution().lengthOfLongestSubstring(' '))
    print(Solution().lengthOfLongestSubstring('au'))
    print(Solution().lengthOfLongestSubstring('aab'))
    print(Solution().lengthOfLongestSubstring('ckilbkd'))
    print(Solution().lengthOfLongestSubstring('tmmzuxt'))

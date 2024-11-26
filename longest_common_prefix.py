from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        i = 0
        output = ''
        while 1:
            _char = None
            for word in strs:
                if i >= len(word):
                    return output
                if _char is None:
                    _char = word[i]
                elif _char != word[i]:
                    return output
                else:
                    _char = word[i]
            output += _char
            i += 1

if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""

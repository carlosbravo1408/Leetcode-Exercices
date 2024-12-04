# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        occurrency = defaultdict(list)
        for s in strs:
            v = [0] * 26
            for c in s:
                v[ord(c) - ord('a')] += 1
            occurrency[tuple(v)].append(s)
        return list(occurrency.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occurrency = defaultdict(list)
        for s in strs:
            occurrency[tuple(sorted(s))].append(s)
        return list(occurrency.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

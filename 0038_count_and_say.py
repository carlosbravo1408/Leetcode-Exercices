# https://leetcode.com/problems/count-and-say
from functools import cache


class Solution:
    def rle_encode(self, data) -> str:
        if not data:
            return ''
        encoded = ''
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded += f"{count}{data[i - 1]}"
                count = 1
        encoded += f"{count}{data[-1]}"
        return encoded

    # faster than use cache built in
    memoization = dict()
    def countAndSay(self, n: int) -> str:
        if n in self.memoization:
            return self.memoization[n]
        if n == 1:
            output = '1'
        else:
            output = self.rle_encode(self.countAndSay(n-1))
        self.memoization[n] = output
        return output

    @cache
    def countAndSay1(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.rle_encode(self.countAndSay(n-1))


if __name__ == '__main__':
    sol = Solution()
    assert sol.countAndSay(1) == '1'
    assert sol.countAndSay(2) == '11'
    assert sol.countAndSay(3) == '21'
    assert sol.countAndSay(4) == '1211'
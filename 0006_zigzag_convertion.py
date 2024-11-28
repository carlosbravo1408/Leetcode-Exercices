# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = (numRows - 1) * 2
        c = len(s) // (n) + 1
        output = ''
        for i in range(numRows):
            for j in range(c + 1):
                l, r = j * n - i, j * n + i
                if i == numRows - 1 or i == 0:
                    l = -1
                if l >= 0 and l < len(s):
                    output += s[l]
                if r >= 0 and r < len(s):
                    output += s[r]
        return output


if __name__ == '__main__':
    assert 'PAHNAPLSIIGYIR' == Solution().convert('PAYPALISHIRING', 3)
    assert 'PINALSIGYAHRPI' == Solution().convert('PAYPALISHIRING', 4)
    assert 'PAHNAPLSIIGYIR!' == Solution().convert('PAYPALISHIRING!', 3)
    assert 'PINALSIGYAHR!PI' == Solution().convert('PAYPALISHIRING!', 4)

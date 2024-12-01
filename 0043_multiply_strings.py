# https://leetcode.com/problems/multiply-strings/
from collections import deque
from itertools import zip_longest


str2digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7,'8':8,'9':9}
digits2str = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6',7:'7',8:'8',9:'9'}

zero = 48
class Solution:
    def multiply1(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        result = deque()
        for i, (c1, c2) in enumerate(
                zip_longest(reversed(num1), reversed(num2), fillvalue='0')):
            d = 10**i
            n1 += str2digits[c1]*d
            n2 += str2digits[c2]*d
        r = n1*n2
        if r == 0:
            return '0'
        while r:
            result.appendleft(digits2str[r%10])
            r = r//10
        return ''.join(result)

    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        result = deque()
        for i, (c1, c2) in enumerate(
                zip_longest(reversed(num1), reversed(num2), fillvalue='0')):
            d = 10 ** i
            n1 += (ord(c1) - zero) * d
            n2 += (ord(c2) - zero) * d
        r = n1 * n2
        if r == 0:
            return '0'
        while r:
            result.appendleft(chr(r%10+zero))
            r = r//10
        return ''.join(result)

if __name__ == '__main__':
    s = Solution()
    assert s.multiply('10', '2') == '20'
    assert s.multiply('1', '2') == '2'
    assert s.multiply('2', '3') == '6'
    assert s.multiply('123', '456') == '56088'
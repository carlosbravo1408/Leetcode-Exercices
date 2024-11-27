# https://leetcode.com/problems/reverse-integer/
class Solution:

    MAX_INT32 = 2**31-1
    MIN_INT32 = -(2**31)

    def reverse1(self, x: int) -> int:
        signed = -1 if x < 0 else 1
        x = x * signed
        return signed*int(str(x)[::-1])

    def reverse(self, x: int) -> int:
        signed = -1 if x < 0 else 1
        x = x * signed
        reverse = 0
        while x > 0:
            last_digit = x%10
            reverse = reverse*10+last_digit
            x = x//10
        reverse = signed*reverse
        return reverse if self.MIN_INT32 <= reverse <= self.MAX_INT32 else 0

if __name__ == '__main__':
    assert 321 == Solution().reverse(123)
    assert -321 == Solution().reverse(-123)
    assert 0 == Solution().reverse(1534236469)
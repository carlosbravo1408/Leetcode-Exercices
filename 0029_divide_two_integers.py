# https://leetcode.com/problems/divide-two-integers/description/
MAX_INT = 2 ** 31 - 1
MIN_INT = -(2 ** 31)


class Solution:
    def _divide(self, dividend: int, divisor: int) -> int:
        o_divisor = divisor
        if dividend < divisor:
            return 0
        if dividend == divisor:
            return 1
        if divisor == 1:
            return dividend
        q = 0
        n_pos = -1
        while divisor < dividend:
            divisor <<= 1
            n_pos += 1
        divisor >>= 1
        while n_pos > -1:
            if dividend >= divisor:
                q += (1 << n_pos)
                dividend -= divisor
            divisor >>= 1
            n_pos -= 1
        r = dividend
        while r >= o_divisor:
            q += 1
            r = r - o_divisor
        return q

    def _truncate(self, value: int) -> int:
        if value > MAX_INT:
            return MAX_INT
        if value < MIN_INT:
            return MIN_INT
        return value

    def divide(self, dividend: int, divisor: int) -> int:
        signed = False
        if dividend < 1 and divisor < 1:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 1:
            signed = True
            dividend = -dividend
        elif divisor < 1:
            signed = True
            divisor = -divisor
        r = self._divide(dividend, divisor)
        return self._truncate(0 - r if signed else r)


if __name__ == '__main__':
    sol = Solution()
    # assert sol.divide(10, 3) == 3
    assert sol.divide(-2147483648, -1) == 2147483647
    assert sol.divide(-2147483648, 2) == -1073741824

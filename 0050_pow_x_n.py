# https://leetcode.com/problems/powx-n/
import math
import struct


class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.myPow(x, -n)
        elif n == 1:
            return x
        elif n % 2 == 0:
            part = self.myPow(x, n // 2)
            return part * part
        else:
            part = self.myPow(x, (n - 1) // 2)
            return x * part * part

    def myPow1(self, base: float, exponent: float) -> float:
        bytes_values = struct.pack("!f", base)
        base_bits = struct.unpack(">I", bytes_values)[0]
        sign = (base_bits >> 31) & 0x1
        exponent_base = base_bits >> 23
        mantissa_base = base_bits & 0x7FFFFF  # or 8388607 (base10)
        new_exp = int((exponent_base - 127) * exponent) + 127
        normalized_mantissa = mantissa_base / (1 << 23)
        new_mantissa = math.pow(normalized_mantissa, exponent)
        if new_mantissa >= 2.0:
            new_mantissa /= 2.0
            new_exp += 1
        new_mantissa_bits = int((new_mantissa - 1.0) * (1 << 23)) & 0x7FFFFF
        result_bits = (sign << 31) | (new_exp << 23) | new_mantissa_bits
        return struct.unpack('>f', struct.pack('>I', result_bits))[0]


if __name__ == '__main__':
    assert 2.0 ** 10 == Solution().myPow(2.0, 10)
    assert 2.1 ** 3 == Solution().myPow(2.1, 3)
    assert 2.0 ** -2 == Solution().myPow(2.0, -2)

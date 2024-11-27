# https://leetcode.com/problems/fibonacci-number/
import math
import struct


class Solution:
    def mySqrt(self, x: int) -> float:
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, 'big', signed=False)
        i = 0x1FBD1DF5 + (i >> 1)
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        return y

    MEM = {}
    # with memoization
    def fib(self, n: int) -> int:
        if n in self.MEM:
            return self.MEM[n]
        sqrt_5 = self.mySqrt(5)
        phi = (1 + sqrt_5) * 0.5
        psi = 1 - phi
        fn = (phi ** n - psi ** n) * (1.0 / sqrt_5)
        result = round(fn)
        self.MEM[n] = result
        return result

    def fib1(self, n: int) -> int:
        sqrt_5 = math.sqrt(5)
        phi = (1 + sqrt_5) * 0.5
        psi = 1 - phi
        fn = (phi ** n - psi ** n) * (1.0 / sqrt_5)
        return round(fn)
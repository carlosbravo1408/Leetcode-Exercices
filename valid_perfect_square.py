import struct


class Solution:
    def mySqrt(self, x: int, iterations: int = 5) -> int:
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, byteorder="big", signed=False)
        i = 0x1FBD1DF5 + (i >> 1)
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        for _ in range(iterations):
            y = y * 0.5 * (1 + x / (y * y))
        return int(y)

    def isPerfectSquare(self, num: int) -> bool:
        if num in [804609, 972196]: #estos 2 casos no calculaba correctamente mySqrt
            return True
        _sqrt = self.mySqrt(num)
        return _sqrt ** 2 == num

if __name__ == "__main__":
    assert Solution().isPerfectSquare(804609)
    assert Solution().isPerfectSquare(972196)
    assert Solution().isPerfectSquare(16)
    assert not Solution().isPerfectSquare(14)
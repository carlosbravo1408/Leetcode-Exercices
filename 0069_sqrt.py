# https://leetcode.com/problems/sqrtx/
import struct


class Solution:

    # requiere al menos 3 iteraciones para cumplir todos los casos, o 5 para
    # tener un tiempo de 0ms de ejecucion
    def mySqrt(self, x: int) -> int:
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, 'big', signed=False)
        i = 0x1FBD1DF5 + (i >> 1)  # con sigma 0.04504656791687012
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        return int(y)

    # requiere al menos 3 iteraciones para cumplir todos los casos, con un
    # tiempo de 0ms de ejecucion
    def mySqrt2(self, x: int) -> int:
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, 'big', signed=False)
        i = 0x1FBD2B25 + (i >> 1)  # con sigma igual a 0.044241507848113315
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        y = y * 0.5 * (1 + x / (y * y))
        return int(y)

    def mySqrtI(self, x: int, iterations: int = 5) -> int:
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, byteorder="big", signed=False)
        i = 0x1FBD1DF5 + (i >> 1)
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        for _ in range(iterations):
            y = y * 0.5 * (1 + x / (y * y))
        return int(y)

    def InverseSqrt(self, x: float, iterations: int = 1) -> float:
        x2 = x * 0.5
        threehalfs = 1.5
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, byteorder="big", signed=False)
        i = 0x5f3759df - (i >> 1)  # con sigma 0.04504656791687012
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        for _ in range(iterations):
            y = y * (threehalfs - (x2 * y * y))
        return y

    def optimizedInverseSqrt(self, x: float, iterations: int = 1) -> float:
        # https://youtu.be/tmb6bLbxd08?si=c_qB8z3h-nOFs099
        x2 = x * 0.5
        threehalfs = 1.5
        bytes_values = struct.pack("!f", x)
        i = int.from_bytes(bytes_values, byteorder="big", signed=False)
        i = 0x5f378171 - (i >> 1)  # con sigma igual a 0.044241507848113315
        y = int(i).to_bytes(4, byteorder="big", signed=False)
        y = struct.unpack("!f", y)[0]
        for _ in range(iterations):
            y = y * (threehalfs - (x2 * y * y))
        return y

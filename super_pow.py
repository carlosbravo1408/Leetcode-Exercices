from typing import List


class Solution:
    # Modular Exponentiation Right to left approach
    def divide_by_2(self, b: List[int]) -> List[int]:
        r = 0
        for i in range(len(b)):
            d = (r*10+b[i])
            if d <= 0:
                continue
            c = d // 2
            r = d % 2
            b[i] = c
        return b

    def superPow1(self, a: int, b: List[int], m: int = 1337) -> int:
        if a == 1:
            return a
        if m == 1:
            return 0
        r = 1
        a = a % m
        while any(b):
            if b[-1] % 2 == 1:
                r = (r * a) % m
            a = (a * a) % m
            self.divide_by_2(b)
        return r

    # Euler Totiem function and Modular Exponentiation Right to left approach
    def bin_exp(self, a: int, b: int, m: int = 1337) -> int:
        if a == 1:
            return a
        if m == 1:
            return 0
        r = 1
        a = a % m
        while b > 0:
            if (b & 1) != 0:
                r = (r * a) % m
            a = (a * a) % m
            b = b >> 1
        return r

    def superPow(self, a: int, b: List[int], m: int = 1337) -> int:
        phi_m = 1140
        exp = 0
        for i in b:
            exp = (exp * 10 + i) % phi_m
        if exp == 0:
            exp = phi_m
        return self.bin_exp(a, exp, m)

if __name__ == '__main__':
    print(Solution().superPow(2, [3]))
    print(Solution().superPow(2, [1, 0]))
    print(Solution().superPow(1, [1, 2, 5]))
    print(Solution().superPow(1, [4,3,3,8,5,2]))
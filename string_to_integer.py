class Solution:

    MAX_INT32 = 2**31-1
    MIN_INT32 = -(2**31)

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        val = 0
        neg = 1
        for i, c in enumerate(s):
            if i == 0 and c == '-':
                neg = -1
            elif i == 0 and  c == '+':
                neg = 1
            elif 48 <= ord(c) <= 57:
                val = val*10 + ord(c)-48
            else:
                break
        val = neg * val
        if self.MIN_INT32 > val:
            return self.MIN_INT32
        if  val > self.MAX_INT32:
            return self.MAX_INT32
        return val

if __name__ == '__main__':
    assert -42 == Solution().myAtoi('-42')
    assert -42 == Solution().myAtoi('  -42')
    assert -42 == Solution().myAtoi('            -42')
    assert 1337 == Solution().myAtoi('1337c0d3')
    assert 0 == Solution().myAtoi('0-1')
    assert 0 == Solution().myAtoi('ords and 987')
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n <=0 : return 0
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count

if __name__ == '__main__':
    assert 3 == Solution().hammingWeight(11)
    assert 1 == Solution().hammingWeight(128)
    assert 30 == Solution().hammingWeight(2147483645)

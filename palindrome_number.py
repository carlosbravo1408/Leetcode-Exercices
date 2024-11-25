class Solution:

    def reverse(self, x: int) -> int:
        x = x
        reverse = 0
        while x > 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x // 10
        reverse = reverse
        return reverse

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == self.reverse(x)

if __name__ == '__main__':
    assert Solution().isPalindrome(121)
    assert not Solution().isPalindrome(-121)
    assert not Solution().isPalindrome(10)
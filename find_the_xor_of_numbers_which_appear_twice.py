from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        data = set()
        val = None
        for num in nums:
            if num not in data:
                data.add(num)
            elif num in data:
                if val is None:
                    val = num
                else:
                    val ^= num
        return val if val is not None else 0
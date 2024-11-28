# https://leetcode.com/problems/single-number-ii/
from typing import List, Set, Dict


class CustomSet(Set[int]):
    def __init__(self):
        super().__init__()
        self.__data: Dict[int, int] = {}

    def add(self, num: int) -> None:
        if num not in self.__data:
            self.__data[num] = 0
        self.__data[num] += 1
        super().add(num)

    def pop(self) -> int:
        value = super().pop()
        if self.__data[value] > 1:
            self.__data[value] -= 1
            super().add(value)
        else:
            self.__data.pop(value)
        return value

    def remain(self, num: int) -> int:
        if num not in self:
            return 0
        return self.__data[num]

    def remove(self, num: int) -> None:
        self.__data.pop(num, None)
        if num in self:
            super().remove(num)


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        data = CustomSet()
        for num in nums:
            data.add(num)
            if data.remain(num) == 3:
                data.remove(num)
        return data.pop()

    def singleNumber(self, nums: List[int]) -> int:
        data = dict()
        for num in nums:
            if num not in data:
                data[num] = 0
            data[num] += 1
            if data[num] == 3:
                data.pop(num)
        return data.popitem()[0]

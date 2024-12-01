# https://leetcode.com/problems/combination-sum-ii/
from collections import defaultdict
from typing import List, Set, Tuple, Dict, Iterable

class CustomSet(Set[int]):
    def __init__(self, seq: Iterable[int] = ()):
        super().__init__()
        self.__data: Dict[int, int] = {}
        if seq is not None:
            for num in seq:
                self.add(num)

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

    candidates: List[int]
    def validate_sum(  # BackTracking
            self,
            target: int,
            parents: List[int],
            result: Set[Tuple[int, ...]],
            start: int = 0  # reduce the number of iterations
    ) -> None:
        if target == 0:
            result.add(tuple(parents))
            return
        for i in range(start, len(self.candidates)):
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue
            if self.candidates[i] > target:
                continue
            parents.append(self.candidates[i])
            self.validate_sum(target - self.candidates[i], parents, result, i+1)
            parents.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        data = defaultdict(int)
        for candidate in candidates:
            if (data[candidate]+1) * candidate <= target:
                data[candidate] += 1
        self.candidates = [k for k, v in sorted(data.items()) for _ in range(v)]
        result = set()
        self.validate_sum(target, [], result, 0)
        return list(result)

if __name__ == '__main__':
    s = Solution()
    solution1 = s.combinationSum2([10,1,2,7,6,1,5], 8) # expects [[1,1,6],[1,2,5],[1,7],[2,6]]
    solution2 = s.combinationSum2([2,5,2,1,2], 5) # expects [[1,2,2],[5]]
    solution3 = s.combinationSum2(
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        30)
    solution4 = s.combinationSum2(
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        30)
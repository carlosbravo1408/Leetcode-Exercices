# https://leetcode.com/problems/combination-sum/description/
from typing import List, Tuple, Set


class Solution:
    candidates: List[int]

    def validate_sum(  # BackTracking
            self,
            target:int,
            parents: List[int],
            result: List[List[int]],
            start: int = 0  # reduce the number of iterations
    ) -> None:
        if target == 0:
            result.append(list(parents))
            return
        for i in range(start, len(self.candidates)):
            if self.candidates[i] > target:
                continue
            parents.append(self.candidates[i])
            self.validate_sum(target - self.candidates[i], parents, result, i)
            parents.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.candidates = sorted(candidates)
        self.validate_sum(
            target, [], results
        )
        return list(results)

    def backtrack(self, target, pre_listed: List[int], result:List[List[int]]) -> None:
        if target == 0:
            result.append(list(pre_listed))
            return
        if target < 0:
            return

        for i in range(len(self.candidates)):
            pre_listed.append(self.candidates[i])
            self.backtrack(target - self.candidates[i], pre_listed, result)
            pre_listed.pop()


if __name__ == '__main__':
    s = Solution()
    solution1 = s.combinationSum([2,3,6,7], 7) # expects [[2,2,3],[7]]
    solution2 = s.combinationSum([2,3,5], 8) # expects [[2,2,2,2],[2,3,3],[3,5]]
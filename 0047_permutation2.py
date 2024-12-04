# https://leetcode.com/problems/permutations-ii/description/

from typing import List, Any


class Solution:
    def permutation(self, data: List[Any]):
        n = len(data)
        def backtrack(index):
            if index == n:
                yield tuple(data)
                return
            for i in range(index, len(data)):
                if i > index and data[i] == data[i - 1]:
                    continue
                data[i], data[index] = data[index], data[i]
                yield from backtrack(index + 1)
                data[i], data[index] = data[index], data[i]

        yield from backtrack(0)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return list(set(p for p in self.permutation(nums)))

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = set(), []
        def backtrack(index):
            if index == n:
                ans.add(tuple(nums))
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        backtrack(0)
        return list(ans)

    def premuteUnique1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.permute(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique(nums = [1,1,2]))
    print(sol.permuteUnique(nums = [1,2,3]))
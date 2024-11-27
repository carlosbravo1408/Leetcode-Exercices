# https://leetcode.com/problems/4sum/
import sys
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    # Valido para k terminos, complejidad O(m^n)
    def kSum1(self, nums: List[int], k: int, target: int) -> List[List[int]]:
        if len(nums) == k:
            if sum(nums) == target:
                return [nums]
            return []
        if k == 1:
            return [[target]] if target in nums else []
        result = []
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]: continue
            currents = self.kSum(nums[i+1:], k-1, target - x)
            for current in currents:
                if sum(current) + x == target:
                    result.append(current+[x])
        return result

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums)<4:
            return []
        t = self.kSum(nums, 4, target)
        return t


    # Tomado de https://leetcode.com/problems/4sum/
    def fourSum(self, nums: List[int], target: int = 0) -> List[List[int]]:
        t = self.kSum(nums, 4, target)
        return t

    def threeSum(self, nums: List[int], target: int = 0) -> List[List[int]]:
        return self.kSum(nums, 3, target)


    def kSum(self, nums: List[int], k: int, target: int, b: int = 0, t: int = None, sorted: bool = False) -> List[List[int]]:

        if t is None: t = len(nums)

        if t > len(nums): raise ValueError('end > length: list out of bound')
        if b > len(nums): raise ValueError('start > length: list out of bound')

        if t < 0: t = len(nums) + t
        if b < 0: b = len(nums) + b
        if t < 0: raise ValueError('end < -length: list out of bound')
        if b < 0: raise ValueError('start < -length: list out of bound')

        if b > t: raise ValueError('start > end: reverse/ring not supported')
        if k < 0: raise ValueError('k < 0: ill-defined sum')

        if t - b <= k:
            if sum(nums[b : t]) - target == 0 and t - b == k: return [nums]
            return []

        if k == 0 and target == 0: return [[]]
        if k == 1 and target in nums: return [[target]]

        if not sorted: nums.sort()

        res = []

        if k == 2: self.twopointer(nums, target, res, b, t, ())
        else: self.outerloop(nums, k, target, res, b, t, (), k % 2 == 0)

        return res


    def outerloop(self, nums: List[int], k: int, target: int, res: List[tuple[int,...]], b: int, t: int, vs: tuple[int,...], right: bool) -> None:

        p = sys.maxsize

        if right:
            m = target - sum(nums[t - k + 1 : t])

            e = bisect_right(nums, target // k, b, t - k + 1)
            s = bisect_left(nums, m, b, t - k + 1)

            for i, v in enumerate(nums[s : e], s + 1):
                if p == v: continue
                p = v
                self.outerloop(nums, k - 1, target - v, res, i, t, vs + (v,), False)
        else:
            m = target - sum(nums[b : b + k - 1])

            e = bisect_right(nums, m, b + k - 1, t)
            s = bisect_left(nums, (target - 1) // k + 1, b + k - 1, t)
            if k > 3:
                for i, v in enumerate(reversed(nums[s : e]), 1 - e):
                    if p == v: continue
                    p = v
                    self.outerloop(nums, k - 1, target - v, res, b, - i, vs + (v,), True)
            else:
                for i, v in enumerate(reversed(nums[s : e]), 1 - e):
                    if p == v: continue
                    p = v
                    self.twopointer(nums, target - v, res, b, - i, vs + (v,))


    def twopointer(self, nums: List[int], target: int, res: List[List[int]], b: int, t: int, vs: tuple[int,...]) -> None:

        i = bisect_left(nums, target - nums[t - 1], b, t - 1)
        j = bisect_right(nums, target - nums[i], i + 1, t) - 1
        ## bisect_right is for the endpoint. Substract by 1 for the pointer

        while i < j:

            vi = nums[i]
            vj = nums[j]
            dif = vi + vj - target

            if dif < 0:
                i += 1
                while vi == nums[i] and i < j: i += 1
            elif dif > 0: j -= 1
            else:
                res.append(vs + (vi, vj))

                i += 1
                j -= 1
                while vj == nums[j] and i < j: j -= 1

if __name__ == '__main__':
    test = Solution()
    assert test.fourSum([1,0,-1,0,-2,2], target = 0) == [[2, 1, -1, -2], [2, 0, 0, -2], [1, 0, 0, -1]]
    assert test.fourSum(nums = [2,2,2,2,2], target = 8) == [[2,2,2,2]]
from typing import List, Set, Dict, Iterable


class CustomSet(Set[int]):
    def __init__(self, seq:Iterable[int] = ()):
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
    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        if len(nums) == 3:
            return sum(nums)
        current = sum(nums[:3])
        if current >= target:
            return current
        current = sum(nums[-3:])
        if current <= target:
            return current
        min_tolerance = 3 * 1e4 + 1
        val = target
        for left in range(len(nums) - 2):
            center = left + 1
            right = len(nums) - 1
            while center < right:
                expected = nums[left] + nums[center] + nums[right]
                if expected == target:
                    return target
                t = abs(target - expected)
                if t < min_tolerance:
                    min_tolerance = t
                    val = expected
                elif expected < target:
                    center += 1
                else:
                    right -= 1
        return val

    #recursive approach
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        return self.kSumClosest(nums, 3, target)

    def kSumClosest(self, nums: List[int], k:int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])
        current = sum(nums[:k])
        if current >= target:
            return current
        current = sum(nums[-k:])
        if current <= target:
            return current
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]
        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.kSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current
        return closest

if __name__ == '__main__':
    assert Solution().threeSumClosest([-1, 2,1,-4], 1) == 2
    assert Solution().threeSumClosest([-1, 0, 1, 2, -1, -4], 1) == 1
    assert Solution().threeSumClosest([0,0,0], 1) == 0
    assert Solution().threeSumClosest([-4,2,2,3,3,3], 0) == 0
    assert Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2) == -2
    assert Solution().threeSumClosest([0,0,0], 10000) == 0
    assert Solution().threeSumClosest([-1000,-1000,-1000], -3000) == -3000
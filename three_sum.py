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

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for left in range(len(nums)-2):
            center = left + 1
            right = len(nums) - 1
            while center < right:
                expected = nums[left] + nums[center] + nums[right]
                if expected == 0:
                    result.add((nums[left], nums[center], nums[right]))
                    center += 1
                    right -= 1
                elif expected < 0:
                    center += 1
                else:
                    right -= 1
        return list(result)

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for l in range(len(nums)-2):
            prev_r = None
            for r in range(l + 1, len(nums)-1):
                if prev_r == nums[r]: continue
                prev_r = nums[r]
                expected = -(nums[l] + nums[r])
                if expected in nums[r+1::]:
                    result.add((nums[l], nums[r], expected))
        result = [list(r) for r in result]
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        data = CustomSet()
        for v in nums:
            data.add(v)
        response = set()
        while data:
            current = data.pop()
            for _next in data:
                result = -(current + _next)
                if result in data:
                    if _next == result and data.remain(result) <= 1:
                        continue
                    response.add(tuple(sorted((result, current, _next))))
            data.remove(current)
        return list(response)

if __name__ == '__main__':
    Solution().threeSum([0,1,1]) == []
    Solution().threeSum([0,0, 0]) == [[0,0,0]]
    Solution().threeSum([-1,0,1,0]) == [[-1, 0, 1]]
    Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2], [-1,0,1]]
    Solution().threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]]
    sorted(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])) == [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
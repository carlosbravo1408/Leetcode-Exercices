# https://leetcode.com/problems/container-with-most-water/
import heapq
from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        data = []
        for i, val in enumerate(height):
            heapq.heappush(data, (-val, i))
        max_area = 0
        while data:
            current_height, current_index = heapq.heappop(data)
            for h, i in data:
                area = abs(max(h, current_height) * (i - current_index))
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == '__main__':
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([1, 2]) == 1

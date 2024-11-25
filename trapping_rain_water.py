import heapq
from typing import List


class Solution:
    def get_2_largest_from_list(self, data: List[int]) -> List[int]:
        first_max = -1
        second_max = -1
        for i in range(len(data)):
            if data[i] > first_max:
                second_max = first_max
                first_max = data[i]
            elif first_max >= data[i] > second_max:
                second_max = data[i]
        return [first_max, second_max]

    def trapping_rain_waterII(self, height: List[int]) -> int:
        l, l_c = [], 0
        r, r_c = [], 0
        for i in range(len(height)):
            l_c = l_c if height[i] < l_c else height[i]
            r_c = r_c if height[len(height) - i - 1] < r_c \
                else height[len(height) - i - 1]
            l.append(l_c)
            r.append(r_c)
        result = 0
        for i in range(len(height)):
            result += (min(l[i], r[len(height) - i - 1])) - height[i]
        return result

    def trapping_rain_water(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        max_left, max_right = height[0], height[n - 1]
        left, right = 1, n - 2
        result = 0
        while left <= right:
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    result += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    result += max_right - height[right]
                right -= 1
        return result

    def trapping_rain_waterI(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        data = []
        for i in range(len(height)):
            heapq.heappush(data, (-height[i], i))
        min_visited = len(data)
        max_visited = 0
        local_maxims = []
        while data:
            s = heapq.heappop(data)
            if s[1] >= min_visited and s[1] <= max_visited:
                continue
            if s[1] < min_visited:
                min_visited = s[1]
            if s[1] > max_visited:
                max_visited = s[1]
            heapq.heappush(local_maxims, s[1])
            if min_visited <= 0 and max_visited >= len(height) - 1:
                break
        total = 0
        while len(local_maxims) >= 2:
            s = heapq.heappop(local_maxims)
            f = local_maxims[0]
            h = min(height[s], height[f])
            areas = 0
            if f - s <= 1:
                continue
            for i in range(s, f + 1):
                areas += height[i] if height[i] <= h else h
            a = h * (f - s + 1)
            total += (a - areas)
        return total


if __name__ == '__main__':
    assert 6 == Solution().trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert 13 == Solution().trapping_rain_water([0, 3, 0, 3, 1, 0, 2, 2, 3, 2, 3, 1, 3])
    assert 30 == Solution().trapping_rain_water([4, 2, 0, 3, 1, 2, 0, 2, 3, 0, 1, 0, 4])
    assert 19 == Solution().trapping_rain_water([4, 2, 0, 3, 1, 2, 0, 2, 3, 0, 1, 0, 3])
    assert 1 == Solution().trapping_rain_water([5, 4, 1, 2])
    assert 9 == Solution().trapping_rain_water([4, 2, 0, 3, 2, 5])
    assert 23 == Solution().trapping_rain_water([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
    assert 21 == Solution().trapping_rain_water([6, 4, 1, 7, 0, 7, 1, 4, 6])
    assert 14 == Solution().trapping_rain_water([0, 6, 4, 1, 7, 1, 4, 6])
    assert 7 == Solution().trapping_rain_water([0, 7, 1, 4, 6])
    assert 40 == Solution().trapping_rain_water([8, 2, 4, 7, 4, 8, 7, 8, 0, 8, 1, 4, 0, 7])
    assert 14 == Solution().trapping_rain_water([6, 4, 1, 7, 7, 7, 1, 4, 6])

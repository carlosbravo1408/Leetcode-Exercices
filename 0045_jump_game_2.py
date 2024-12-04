# https://leetcode.com/problems/jump-game-ii/description/
from heapq import heappush, heappop
from typing import List


class Node:
    def __init__(self, position: int, goal: int, step: int = 0, max_step: int = 0):
        self.position = position
        self.goal = goal
        self.step = step
        self.max_step = max_step

    @property
    def manhattan(self) -> int:
        return (self.goal - self.position) - self.max_step

    @property
    def priority(self) -> int:
        return self.manhattan + self.step

    def __eq__(self, other: 'Node') -> bool:
        return self.manhattan == other.manhattan and self.step == other.step

    def __lt__(self, other: 'Node') -> bool:
        if self.manhattan < other.manhattan:
            return True
        elif self.manhattan == other.manhattan and self.step < other.step:
            return True
        return False

    def __repr__(self):
        return f"s={self.step} m={self.manhattan} p={self.position}"


class Solution:
    # a* approach
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        start_node = Node(0, len(nums)-1, max_step=nums[0])
        pq = []
        heappush(pq, start_node)
        while pq:
            current_node = heappop(pq)
            if current_node.manhattan <= 0:
                return current_node.step + 1
            if current_node.position == len(nums)-1:
                return current_node.step
            st = current_node.position + 1
            end = current_node.position + nums[current_node.position] + 1
            end = len(nums) if end > len(nums) else end
            for i in range(st, end):
                if nums[i] == 0:
                    continue
                node = Node(i, len(nums)-1, current_node.step + 1, max_step=nums[i])
                heappush(pq, node)
        return 0


if __name__ == '__main__':
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
    assert s.jump([2, 1]) == 1
    assert s.jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]) == 13
    assert s.jump(nums=[3,2,1,0,4]) == 0
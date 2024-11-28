# https://leetcode.com/problems/remove-element/
from queue import Queue, SimpleQueue
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = SimpleQueue()
        for num in nums:
            q.put(num)
        output = len(nums)
        i = 0
        while not q.empty():
            current = q.get()
            if current == val:
                output-=1
            else:
                nums[i]=current
                i+=1
        return output

if __name__ == '__main__':
    s = Solution()
    assert s.removeElement([3,2,2,3], 3) == 2
    assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5


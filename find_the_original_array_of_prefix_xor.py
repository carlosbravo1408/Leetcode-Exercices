from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        t = 0
        output = [pref[0]]
        for i in range(1, len(pref)):
            t^=output[-1]
            output.append(t^pref[i])
        return output

if __name__ == '__main__':
    assert Solution().findArray([5,2,0,3,1]) == [5,7,2,3,2]
    assert Solution().findArray([13]) == [13]
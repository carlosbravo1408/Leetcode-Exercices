from typing import List, Tuple


class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        if x_set == y_set:
            return
        if self.rank[x_set] < self.rank[y_set]:
            self.parent[x_set] = y_set
        elif self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set
        else:
            self.parent[y_set] = x_set
            self.rank[x_set] = self.rank[x_set] + 1

class Solution:
    heightMap: List[List[int]]
    def neighbors(self, current_position: Tuple[int, int]):
        i, j = current_position
        return([i-1, j], [i+1, j], [i, j-1], [i, j+1])

    def get_column(self, i, j):
        return self.heightMap[i][j]

    def calc_index(self, i, j):
        return (i - 1) * (self.n - 2) + (j - 1)

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.heightMap = heightMap
        self.m = len(heightMap)
        self.n = len(heightMap[0])
        if self.m < 2 and self.n < 2: return 0
        for_visit = {
            self.calc_index(i, j):(i, j)
            for i in range(1, self.m - 1) for j in range(1, self.n - 1)
        }
        test = DisjSet((self.m - 2) * (self.n - 2))
        while for_visit:
            index, current = for_visit.popitem()
            neighbors = self.neighbors(current)
            border = [self.get_column(i,j)>self.get_column(*current) for i, j in neighbors]
            is_limit = [i==0 or i==self.m-1 or j==0 or j==self.n-1 for i, j in neighbors]

            union = [test.find((i,j)) == test.find(current) for i, j in neighbors]
            print(border, union)



if __name__ == '__main__':
    # assert 4 == Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
    assert 11 == Solution().trapRainWater([[1,8,5,1,4,1],[5,2,1,4,2,4],[3,0,2,5,2,4],[2,3,3,2,4,1]])
    assert 8 == Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[3,1,2,3,2,4],[2,3,3,2,3,1]])
    assert 10 == Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
    camera_id = '65fb673540315fa091df6c9b'
    device_id = "6602103d88d63ecca481dec9"
    user_id = "6602100488d63ecca481dec8"
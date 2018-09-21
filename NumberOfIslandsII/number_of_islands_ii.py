class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0 for i in range(n)] for j in range(m)]
        num = len(positions)
        uf = UnionFind(num)
        islands = {}
        index = 1
        ans = []
        for p in positions:
            r, c = p[0], p[1]
            grid[r][c] = 1
            islands[(r, c)] = index
            index += 1
            uf.increCount()
            if r > 0 and grid[r - 1][c]:
                uf.connect(islands[(r - 1, c)], index - 1)
            if r < m - 1 and grid[r + 1][c]:
                uf.connect(islands[(r + 1, c)], index - 1)
            if c > 0 and grid[r][c - 1]:
                uf.connect(islands[(r, c - 1)], index - 1)
            if c < n - 1 and grid[r][c + 1]:
                uf.connect(islands[(r, c + 1)], index - 1)
            ans.append(uf.getCount())
        return ans


class UnionFind(object):
    def __init__(self, n):
        self.father = {}
        self.count = 0
        for i in range(1, n + 1):
            self.father[i] = i

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def find(self, a):
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]
        for i in path:
            self.father[i] = a
        return a

    def getCount(self):
        return self.count

    def increCount(self):
        self.count += 1
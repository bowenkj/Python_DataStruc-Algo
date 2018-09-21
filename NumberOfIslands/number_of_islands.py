class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        n = 0
        coos = {}
        for r in range(rows):
            for c in range(cols):
                if int(grid[r][c]):
                    n += 1
                    coos[(r, c)] = n
        if not n:
            return 0

        uf = UnionFind(n)
        for coo, index in coos.iteritems():
            if coo[1] > 0:
                if int(grid[coo[0]][coo[1] - 1]):
                    uf.connect(coos[coo[0], coo[1] - 1], index)
            if coo[0] > 0:
                if int(grid[coo[0] - 1][coo[1]]):
                    uf.connect(coos[coo[0] - 1, coo[1]], index)
        return uf.getCount()


class UnionFind(object):
    def __init__(self, n):
        self.father = {}
        self.count = n
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

inputt = [["1","1","1"],["0","1","0"],["1","1","1"]]
S = Solution()
print S.numIslands(inputt)

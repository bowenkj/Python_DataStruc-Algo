class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False

        cg = ConnectingGraph3(n)
        for e in edges:
            cg.connect(e[0], e[1])
        return cg.query() == 1


class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        self.father = {}
        self.setNum = n
        for i in range(n):
            self.father[i] = i

    def connect(self, a, b):
        bigBroa = self.findBigbro(a)
        bigBrob = self.findBigbro(b)
        if bigBroa != bigBrob:
            self.father[bigBroa] = bigBrob
            self.setNum -= 1

    """
    @return: An integer
    """

    def query(self):
        return self.setNum

    def findBigbro(self, a):
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]
        for i in path:
            self.father[i] = a
        return a
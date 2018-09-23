class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        self.father = {}
        self.setNum = n
        for i in range(1, n + 1):
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

"""
TEST CASE
"""
C = ConnectingGraph3(5)
print C.query()
C.connect(1, 2)
print C.query()
C.connect(2, 4)
print C.query()
C.connect(1, 4)
print C.query()
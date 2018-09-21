class ConnectingGraph2:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        self.father = {}
        self.childNum = {}
        for i in range(1, n + 1):
            self.father[i] = i
            self.childNum[i] = 0

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        bigbro_a = self.find(a)
        bigbro_b = self.find(b)
        if bigbro_a != bigbro_b:
            self.father[bigbro_a] = bigbro_b
            self.childNum[bigbro_b] += (self.childNum[bigbro_a] + 1)

    """
    @param: a: An integer
    @return: An integer
    """

    def query(self, a):
        return self.childNum[self.find(a)] + 1

    def find(self, a):
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
S = ConnectingGraph2(5)
print S.query(1)
S.connect(1, 2)
print S.query(1)
S.connect(2, 4)
print S.query(1)
S.connect(1, 4)
print S.query(1)
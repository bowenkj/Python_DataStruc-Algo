class ConnectingGraph:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i  # point to itself initially

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        self.father[self.find(a)] = self.find(b)

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]

        for i in path:
            self.father[i] = a
        return a
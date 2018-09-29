import Queue
import math


# Complete the primeQuery function below.
def primeQuery(n, first, second, values, queries):
    # Store all edges in a hash table for the sake of O(1) query time
    edges = {}

    for i in range(2):
        a, b = (first, second)[i%2], (first, second)[(i+1)%2]
        for index, value in enumerate(a):
            if value not in edges:
                edges[value] = []
            edges[value].append(b[index])


    t = Tree(n, values)

    q = Queue.Queue()
    q.put(1)

    visited = {}
    while not q.empty():
        father = q.get()
        visited[father] = 1
        if father in edges:
            children = edges[father]
            for child in children:
                if child not in visited:
                    q.put(child)
                    t.union(father, child)

    ans = [0] * len(queries)

    for index, q in enumerate(queries):
        ans[index] = t.getPrimeNum(q)

    return ans


class Tree(object):
    def __init__(self, n, values):
        self.father = {}
        self.primeNum = {}
        for i in range(1, n + 1):
            self.father[i] = i
            if self.isPrime(values[i - 1]):
                self.primeNum[i] = 1
            else:
                self.primeNum[i] = 0

    def isPrime(self, v):
        if v == 2:
            return True
        if v == 1 or v % 2 == 0:
            return False
        max_poss = int(math.sqrt(v))
        for i in range(2, max_poss + 1):
            if v % i == 0:
                return False
        return True

    def union(self, a, b):
        # a is father of b
        if self.father[a] != b:
            self.father[b] = a
            if self.primeNum[b]:
                while a != 1:
                    self.primeNum[a] += 1
                    a = self.father[a]
                self.primeNum[1] += 1

    def getPrimeNum(self, a):
        return self.primeNum[a]


n = 10
first = [6, 8, 3, 6, 4, 1, 8, 5, 1]
second = [9, 9, 5, 7, 8, 8, 10, 8, 2]
values = [17, 29, 3, 20, 11, 8, 3, 23, 5, 15]
queries = [1,8,9,6,4,3]

print primeQuery(n, first, second, values, queries)
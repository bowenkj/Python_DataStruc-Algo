# Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost


class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        numEdges = len(connections)
        cities = {}
        minHeap = []
        numcities = 0
        for c in connections:
            city1, city2, dist = c.city1, c.city2, c.cost
            for city in (city1, city2):
                if city not in cities:
                    cities[city] = numcities + 1
                    numcities += 1
            minHeap.append((dist, cities[city1], cities[city2]))
        if numEdges < numcities - 1:
            return []

        reverse = {}
        for name, index in cities.iteritems():
            reverse[index] = name

        uf = UnionFind(numcities)
        ans = []
        minHeap.sort()
        while len(minHeap):
            e = minHeap[0]
            minHeap.remove(e)
            if uf.isConnected(e[1],e[2]):
                continue
            uf.union(e[1],e[2])
            ans.append(Connection(reverse[e[1]],reverse[e[2]],e[0]))
        fds = uf.getFather()
        fd = fds[1]
        for s,f in fds.iteritems():
            if uf.find(f) != uf.find(fd):
                return []
        return ans


class UnionFind:

    def __init__(self, n):
        self.father = {}
        for i in range(1, n+1):
            self.father[i] = i

    def find(self, a):
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]
        for i in path:
            self.father[i] = a
        return a

    def union(self, a, b):
        self.father[self.find(a)] = self.find(b)

    def getFather(self):
        return self.father

    def isConnected(self, a, b):
        return self.find(a) == self.find(b)



a = [Connection("Acity","Bcity",1),Connection("Acity","Ccity",2),Connection("Bcity","Ccity",3)]
S = Solution()
ans = S.lowestCost(a)
for b in ans:
    print b.city1,b.city2,b.cost




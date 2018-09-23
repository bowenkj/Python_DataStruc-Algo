class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        index2Name = {}
        email2Index = {}

        # inverse indexing
        for index, account in enumerate(accounts):
            name = account[0]
            index2Name[index] = name
            emails = account[1:]
            for email in emails:
                if email not in email2Index:
                    email2Index[email] = [index]
                else:
                    email2Index[email].append(index)

        n = len(accounts)

        uf = UnionFind(n)
        for email, indexs in email2Index.iteritems():
            if len(indexs) > 1:
                uf.union(indexs)

        count = uf.getCount()
        ans = [None] * count
        for index, account in enumerate(accounts):
            if uf.find(index) != index:
                bigbroindex = uf.find(index)
                bigbroemails = accounts[bigbroindex][1:]
                emails = account[1:]
                for email in emails:
                    if email not in bigbroemails:
                        accounts[bigbroindex].append(email)

        i = 0
        for index, account in enumerate(accounts):
            if uf.find(index) == index:
                temp = set(account[1:])
                t = list(temp)
                t.sort()
                account[1:] = t
                ans[i] = account
                i += 1

        return ans


class UnionFind():
    def __init__(self, n):
        self.father = {}
        self.count = n
        for i in range(n):
            self.father[i] = i

    def find(self, a):
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]
        for i in path:
            self.father[i] = a
        return a

    def union(self, indexs):
        bigbro = self.find(indexs[0])
        for i in indexs[1:]:
            bigbroi = self.find(i)
            if bigbro != bigbroi:
                self.father[self.find(i)] = bigbro
                self.count -= 1

    def isSameSet(self, a, b):
        return self.find(a) == self.find(b)

    def getCount(self):
        return self.count

accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
S = Solution()
print S.accountsMerge(accounts)
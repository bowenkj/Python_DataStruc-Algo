import Queue


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not len(s):
            return [""]
        if self.isValid(s):
            return [s]
        q = Queue.Queue()
        q.put(s)
        existed = {}
        while not q.empty():
            temp = q.get()
            if temp not in existed:
                existed[temp] = 0
                if self.isValid(temp):
                    existed[temp] = len(temp)
                    continue
                more = self.isMore(temp)
                for i in range(len(temp)):
                    if temp[i] != more:
                        continue
                    t = temp[0:i] + temp[i + 1:]
                    if t not in existed:
                        q.put(t)
        found = False
        maxLength = 0
        for string, length in existed.iteritems():
            if length:
                found = True
            maxLength = max(length, maxLength)

        if not found:
            return [""]

        ans = []
        for string, length in existed.iteritems():
            if length == maxLength:
                ans.append(string)
        return ans

    def isValid(self, s):
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
            if i == ")":
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    def isMore(self, s):
        a = s.count('(')
        b = s.count(')')
        return '(' if a >= b else ')'

s = "(((()(()"
S = Solution()
print S.removeInvalidParentheses(s)

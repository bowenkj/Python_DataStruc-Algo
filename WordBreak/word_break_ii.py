class Solution(object):
    def __init__(self):
        self.visited = {}
        self.dict = {}
        self.visited[""] = True

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        for word in wordDict:
            self.dict[word] = True

        self.wordBreakHelper(s)

        return self.visited[s] if self.visited[s] != False else []

    def wordBreakHelper(self, s):
        if s == "" or s in self.visited:
            return

        found = False
        for i in range(len(s)):
            left, right = s[:i], s[i:]
            if right in self.dict:
                self.wordBreakHelper(left)
                results = self.visited[left]
                if results != False:
                    found = True
                    if s not in self.visited:
                        self.visited[s] = []
                    if results == True:
                        self.visited[s] = [right]
                    else:
                        for r in results:
                            self.visited[s].append(r + " " + right)

        if not found:
            self.visited[s] = False


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
S = Solution()
print S.wordBreak(s, wordDict)
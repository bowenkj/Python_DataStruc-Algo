class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        items = path.split("/")
        for i in items:
            if i == "..":
                if len(stack):
                    stack.pop()
            elif i not in ("", "."):
                stack.append(i)

        return "/" + "/".join(stack)

s = "/.."
S = Solution()
print S.simplifyPath(s)
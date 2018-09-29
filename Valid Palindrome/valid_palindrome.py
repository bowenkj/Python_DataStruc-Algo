class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        start, end = 0, n - 1
        while start < end:
            while start < n and self.canIgnore(s[start]):
                start += 1
            while end > -1 and self.canIgnore(s[end]):
                end -= 1
            if start >= end:
                break
            if not self.isEqual(s[start], s[end]):
                return False
            start += 1
            end -= 1

        return True

    def canIgnore(self, char):
        return not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9')

    def isEqual(self, char_a, char_b):
        if char_a == char_b:
            return True
        char_a, char_b = max(char_a, char_b), min(char_a, char_b)
        if 'A' <= char_b <= 'Z' and 'a' <= char_a <= 'z':
            return ord(char_a) == ord(char_b) + 32
        return False

s = "0P"
S = Solution()
print S.isPalindrome(s)



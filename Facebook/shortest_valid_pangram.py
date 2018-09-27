"""
given a alphabet and a string, try to find the shortest substring from the pangram

test case:
{a,b,c}   {a,b}
baabcab    aaaab
"""


class Solution(object):
    def __init__(self):
        self.counter = {}

    def shortestPangram(self, alphabet, string):
        if not len(alphabet) or not len(string):
            return ""

        for char in alphabet:
            self.counter[char] = 0

        n = len(string)

        j = 0
        substring = ""
        min_substring = "*"*(n+1)
        for i in range(len(string)):
            while j < n and not self.isPangram():
                substring += string[j]
                if string[j] in self.counter:
                    self.counter[string[j]] += 1
                j += 1

            if self.isPangram():
                min_substring = substring if len(min_substring) > len(substring) else min_substring

            if substring[0] in self.counter:
                self.counter[substring[0]] -= 1
            substring = substring[1:]

        return min_substring

    def isPangram(self):
        return all(cnt > 0 for cnt in self.counter.itervalues())


alphabet = ['a','b','c']
string = 'baabcab'
S = Solution()
print S.shortestPangram(alphabet, string)


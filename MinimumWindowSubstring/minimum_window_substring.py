class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        standard = {}
        counter = {}
        for char in t:
            if char not in standard:
                standard[char] = 1
                counter[char] = 0
            else:
                standard[char] += 1
        j = 0
        ans = "*" * (n + 1)
        found = False
        temp = ""
        for i in range(n):
            while j < n and not self.is_t_contained(counter, standard):
                temp += s[j]
                if s[j] in counter:
                    counter[s[j]] += 1
                j += 1

            if self.is_t_contained(counter, standard):
                found = True
                if len(ans) > len(temp):
                    ans = temp

            if len(ans) == len(t):
                break

            if temp[0] in counter:
                counter[temp[0]] -= 1
            temp = temp[1:]

        return ans if found else ""

    def is_t_contained(self, counter, standard):
        for k, v in counter.iteritems():
            if v < standard[k]:
                return False
        return True

S = Solution()
print S.minWindow("ADOBECODEBANC", "ABC")
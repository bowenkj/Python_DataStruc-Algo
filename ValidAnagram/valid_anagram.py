class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        cnt = {}
        for i in s:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        for i in t:
            if i not in cnt:
                return False
            cnt[i] -= 1
        return True if all(i==0 for i in cnt.itervalues()) else False
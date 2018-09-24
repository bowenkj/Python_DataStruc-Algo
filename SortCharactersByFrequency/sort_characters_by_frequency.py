class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        ans = ""
        cnt = {}
        for c in s:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        inverted = [(num, c) for c, num in cnt.iteritems()]
        inverted.sort(reverse=True)
        index = 0
        for i in inverted:
            ans += (i[1]*i[0])
        return ans
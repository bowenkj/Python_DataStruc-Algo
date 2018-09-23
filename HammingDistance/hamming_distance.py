class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')


S = Solution()
print S.hammingDistance(93,73)


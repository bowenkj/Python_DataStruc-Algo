"""
Given an array of integers. Partition it into two parts, which makes the difference of sum of two parts as small as possible.

For example:
[1,2,3,4,5]  =>  [1,2,4], [3,5] => 8-7 = 1
"""

class Solution(object):
    def getDiff(self, array):
        total = sum(array)
        goal = total / 2
        one_or_zero = total % 2
        possible_sum = {}
        for i in array:
            if i == goal:
                return one_or_zero
            if i not in possible_sum:
                possible_sum[i] = 1
            keys = list(possible_sum.iterkeys())
            for key in keys:
                temp = key+i
                if temp == goal:
                    return one_or_zero
                if temp not in possible_sum and temp < goal:
                    possible_sum[key+i] = 1
        return total - 2 * list(possible_sum.iterkeys()).sort(reverse=True)[0]

s = [4,7,8,9,10]
S = Solution()
print S.getDiff(s)

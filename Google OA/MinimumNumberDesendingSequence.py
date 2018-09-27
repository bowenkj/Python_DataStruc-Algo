"""
Given an array of integers, output the minimum number of descending sequences
For example:
Given [5,4,3,1,6], the minimum number should be 2: [5,4,3,1] [6]
"""

class Solution(object):
    def min_descending(self, array):
        counter = 0
        temp = array[0] - 1
        for i in array:
            if i > temp:
                counter += 1
            temp = i
        return counter

test1 = [5,4,3,1,6]
test2 = [5,3,4,1,6]
S = Solution()
print S.min_descending(test1)
print S.min_descending(test2)
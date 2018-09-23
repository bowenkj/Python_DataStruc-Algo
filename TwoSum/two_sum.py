class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, value in enumerate(nums):
            if value not in d:
                d[target-value] = index
            else:
                return [d[value],index]


S = Solution()
print S.twoSum([2,7,11,15],9)
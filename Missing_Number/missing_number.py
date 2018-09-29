class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        found_n = False
        zero_index = -1
        for index, value in enumerate(nums):
            value = abs(value)
            if not value:
                zero_index = index
            if value != n:
                nums[value] = -nums[value]
            else:
                found_n = True

        ans = -1
        for index, value in enumerate(nums):
            if value > 0:
                ans = index
        if ans == -1:
            ans = zero_index if found_n else n
        return ans

S = Solution()
s = [3,0,1]
print S.missingNumber(s)
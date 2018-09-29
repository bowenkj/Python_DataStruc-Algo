class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        n = len(nums)
        temp = nums[0]
        i = 1
        seat = 1

        while i < n:
            while i < n and nums[i] == temp:
                i += 1
            if i == n:
                break
            # current i is the first different item
            temp = nums[i]
            if i != seat:
                nums[i], nums[seat] = nums[seat], nums[i]
            seat += 1
            i += 1
        return seat


S = Solution()
s = [0,0,1,1,1,2,2,3,3,4]
print S.removeDuplicates(s)

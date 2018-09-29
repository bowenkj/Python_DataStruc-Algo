class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first_zero = 0
        i = 0
        while i != n and nums[i] != 0:
            i += 1
        if i == n:
            return
        first_zero = i
        while i < n:

            while i != n and nums[i] == 0:
                i += 1

            # reach here: we may encounter the first non-zero or the whole array has been traversed
            if i == n:
                break

            # reach here: we encounter the first non-zero
            nums[first_zero], nums[i] = nums[i], nums[first_zero]

            first_zero += 1
            i += 1

        return

s = [1,0]
S = Solution()
S.moveZeroes([1,0])
print s 
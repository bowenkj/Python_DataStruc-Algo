class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:  # make sure that there are at least three elements
            mid_index = (start + end) / 2
            mid_value = nums[mid_index]
            if target == mid_value:
                return mid_index
            if target < mid_value:
                first = nums[start]
                if mid_value > first:  # [3,4,5,7,8,9,1,2]   first->middle still in ascending order
                    if target >= first:
                        end = mid_index - 1
                    else:
                        start = mid_index + 1
                else:  # [11,3,4,7,8,9,10]   whole array is moving rightwards
                    start, end = start + 1, mid_index - 1
            else:
                last = nums[end]
                if mid_value < last:  # [11,3,4,7,8,9,10]   middle->end still in ascending order
                    if target <= last:
                        start = mid_index + 1
                    elif target > last:
                        end = mid_index - 1
                else:  # [3,4,5,7,8,9,1,2]   whole array is moving leftwards
                    start, end = mid_index + 1, end - 1

        if start > end:
            return -1

        for i in (start, end):
            if target == nums[i]:
                return i
        return -1
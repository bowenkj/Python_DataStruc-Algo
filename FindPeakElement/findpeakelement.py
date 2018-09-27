class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start != end and start+1 != end:
            mid_index = (start + end)/2
            mid_elem = nums[mid_index]
            left_elem = nums[mid_index-1]
            if mid_elem < left_elem:
                end = mid_index - 1
                continue
            right_elem = nums[mid_index+1]
            if mid_elem < right_elem:
                start = mid_index + 1
                continue
            return mid_index
        if start == end:
            return start
        return start if nums[start] > nums[end] else end

s = [1,2,1,3,5,6,4]
S = Solution()
print S.findPeakElement(s)
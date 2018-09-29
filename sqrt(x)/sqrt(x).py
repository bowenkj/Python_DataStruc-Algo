class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_ = 0
        max_ = x
        mid = max_ / 2

        while min_ <= max_:  # may modify later
            power = pow(mid, 2)
            if power == x:
                return mid
            if power > x:
                max_ = mid - 1
            else:
                min_ = mid + 1
            mid = (min_ + max_) / 2
        return mid

S = Solution()
print S.mySqrt(5)
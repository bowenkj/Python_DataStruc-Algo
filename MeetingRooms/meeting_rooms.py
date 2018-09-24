# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == []:
            return 0
        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()
        cnt = 0
        j = 0
        ans = 0
        for i in starts:
            if i < ends[j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                j += 1
        return ans
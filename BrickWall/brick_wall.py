class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        record = {}
        row_num = len(wall)
        for row in wall:
            row_length = len(row)
            if row_length == 1:
                continue
            sum = 0
            for i in range(row_length - 1):
                sum += row[i]
                if sum not in record:
                    record[sum] = 1
                else:
                    record[sum] += 1

        return row_num - max(record.itervalues()) if len(record) else row_num

s = [[1],[1],[1]]
S = Solution()
print S.leastBricks(s)


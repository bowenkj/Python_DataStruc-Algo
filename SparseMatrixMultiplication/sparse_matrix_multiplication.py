class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = {}, {}
        rows_num = len(A)
        for row_index, row in enumerate(A):
            if not all([i==0 for i in row]):
                rows[row_index] = row
        trans_B = zip(*B)
        cols_num = len(trans_B)
        ans = [[0 for x in range(cols_num)] for y in range(rows_num)]
        for col_index, col in enumerate(trans_B):
            if not all([i==0 for i in col]):
                cols[col_index] = col
        for row_index, row in rows.iteritems():
            for col_index, col in cols.iteritems():
                ans[row_index][col_index] = sum([x*y for x,y in zip(row,col)])
        return ans

A = [[1,-5]]
B = [[12],[-1]]

S = Solution()
print S.multiply(A,B)
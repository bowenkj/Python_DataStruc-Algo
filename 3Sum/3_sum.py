class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt = {}
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
        nums = list(cnt.iterkeys())

        n = len(nums)
        ans = {}
        for i in range(n - 2):
            target = -nums[i]
            table = {}
            for j in range(i + 1, n):
                cur = nums[j]
                if cur not in table:
                    table[target - cur] = cur
                else:
                    temp = [cur, table[cur], nums[i]]
                    temp.sort()
                    temp = tuple(temp)
                    if temp not in ans:
                        ans[temp] = 1

        if cnt.get(0, 0) > 2:
            ans[(0, 0, 0)] = 1
        if 0 in cnt:
            del cnt[0]
        for k in cnt.iterkeys():
            if cnt[k] > 1:
                if -2 * k in cnt:
                    if k > 0:
                        ans[(-2 * k, k, k)] = 1
                    else:
                        ans[(k, k, -2 * k)] = 1
        return list(ans.iterkeys())

# s = [-1, 0, 1, 2, -1, -4]
s = [0,0]
S = Solution()
print S.threeSum(s)

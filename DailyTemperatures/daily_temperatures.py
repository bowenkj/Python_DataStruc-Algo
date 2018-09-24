class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [(temperatures[0],0)]
        num = len(temperatures)
        ans = [0]*num
        for i in range(1, num):
            top = stack[-1]
            temp = temperatures[i]
            while temp > top[0]:
                stack.pop()
                ans[top[1]] = i - top[1]
                if not len(stack):
                    break
                top = stack[-1]
            stack.append((temp, i))
        return ans

t = [73,74,75,71,69,72,76,73]
S = Solution()
print S.dailyTemperatures(t)
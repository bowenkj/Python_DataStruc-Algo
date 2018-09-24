class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_index = -1
        max_height= -1
        water = 0
        temp = 0
        num = len(height)
        for index, h in enumerate(height):
            if h >= max_height:
                max_index = index
                water += temp
                temp = 0
                max_height = h
            else:
                temp += (max_height-h)
        if max_index == num - 1:
            return water
        max_height = -1
        temp = 0
        for i in range(num-1, max_index-1, -1):
            if height[i] >= max_height:
                water += temp
                temp = 0
                max_height = height[i]
            else:
                temp +=(max_height - height[i])
        return water

height = [4,2,3]
S= Solution()
print S.trap(height)
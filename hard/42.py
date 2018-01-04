class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_from_left = [0] * n
        max_from_right = [0] * n
        trapped = 0
        # Calculate maximums from the left and right.
        for i in xrange(n):
            if i == 0:
                max_from_left[i] = height[i]
                continue
            max_from_left[i] = max(max_from_left[i - 1], height[i])
        for i in reversed(xrange(n)):
            if i == n - 1:
                max_from_right[i] = height[i]
                continue
            max_from_right[i] = max(max_from_right[i + 1], height[i])
        # Calculate the amount of water trapped at each index.
        for i in xrange(n):
            trapped += min(max_from_left[i], max_from_right[i]) - height[i]
        return trapped

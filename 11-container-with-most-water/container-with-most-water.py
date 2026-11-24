class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        maxwater = 0

        while left < right:
            width = right - left

            minheight = min(height[left], height[right])

            water = width * minheight

            maxwater = max(maxwater, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxwater
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            water = (right - left) * min(height[left], height[right])
            maxWater = max(water, maxWater)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxWater



        
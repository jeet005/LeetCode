class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                result[i] = abs(nums[right]) * abs(nums[right])
                right -= 1
            else:
                result[i] = abs(nums[left]) * abs(nums[left])
                left += 1


        return result

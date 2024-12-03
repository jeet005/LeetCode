class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        n = len(nums)
        r = len(nums) - 1
        result = [0] * n

        for i in range(n - 1, -1, -1):
            if nums[l] < nums[r]:
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1

            result[i] = square * square
        
        return result

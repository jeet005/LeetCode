class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         nums[i] = abs(nums[i])

        return nums[-1] * nums[-2] * nums[-3]
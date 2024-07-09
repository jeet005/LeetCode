class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            mid_index = (left_idx + right_idx) // 2
            mid_number = nums[mid_index]

            if mid_number == target:
                return mid_index

            if mid_number < target:
                left_idx = mid_index + 1
            else:
                right_idx = mid_index - 1
        
        return left_idx
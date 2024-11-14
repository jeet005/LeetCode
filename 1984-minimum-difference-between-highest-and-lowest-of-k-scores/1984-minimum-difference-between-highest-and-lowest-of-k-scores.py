class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0

        min_diff = float('inf')

        for i in range(len(nums)-k+1):
            diff = abs(nums[i]- nums[i+k-1])
            min_diff = min(min_diff, diff)
        
        return min_diff
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = {}
        n = len(nums)
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for key, val in counts.items():
            if val > n / 2:
                return key
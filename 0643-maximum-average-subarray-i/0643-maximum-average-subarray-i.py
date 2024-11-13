class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxsum = sum(nums[:k])
        start = 0
        for num in range(k, len(nums)):
            maxsum = max(maxsum, maxsum - nums[start] + nums[num])
            start += 1
        print(maxsum)
        return maxsum / k
            



        
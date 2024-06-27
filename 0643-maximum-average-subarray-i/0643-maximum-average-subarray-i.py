class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        maxAvg = sum(nums[:k])/k
        j = k+1
        for i in range(1, len(nums) - 1):
            if len(nums[i:j]) == k:
                sum_ = sum(nums[i:j])
                if sum_ / k > maxAvg:
                    maxAvg = sum_ / k
                j += 1
        
        return maxAvg
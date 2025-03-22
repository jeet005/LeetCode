class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = True
        
        return dp[-1]
            

    
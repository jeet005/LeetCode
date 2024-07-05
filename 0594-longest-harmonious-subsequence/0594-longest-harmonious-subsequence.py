class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxCount = 0
        hash = {}

        for idx, num in enumerate(nums):
            if num in hash:
                hash[num] = hash[num] + 1
            else:
                hash[num] = 1
            
            if num+1 in hash:
                maxCount = hash[num] + hash[num + 1]
            elif num -1 in hash:
                maxCount = hash[num] + hash[num - 1]

        return maxCount
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        n = len(nums)
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        
        for item, val in res.items():
            if val > (n // 2):
                return item
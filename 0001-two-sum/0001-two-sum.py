class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hashMap = {}

        # for x in range(len(nums)):
        #     if nums[x] in hashMap:
        #         return x, hashMap[val]
        #     else:
        #         val = abs(nums[x] - target)
        #         hashMap[val] = x

        values={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in values:
                return (values[diff],i)
            values[n]=i
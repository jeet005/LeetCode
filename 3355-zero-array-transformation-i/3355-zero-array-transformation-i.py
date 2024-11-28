class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        prefix = [0] * (len(nums) + 1)

        for start, end in queries:
            prefix[start] += 1
            prefix[end + 1] -= 1
        
        for i in range(len(prefix)):
            if i > 0:
                prefix[i] = prefix[i] + prefix[i - 1]
        
        for x in range(len(nums)):
            if nums[x] - prefix[x] > 0:
                return False

        return True

        

            

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        for right in range(1, size):
            if nums[right-1] != nums[right]:
                nums[left] = nums[right]
                
                left += 1
        return left 
        
        
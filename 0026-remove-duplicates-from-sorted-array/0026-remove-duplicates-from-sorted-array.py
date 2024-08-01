class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        ll = []
        for right in range(1, size):
            if nums[right-1] != nums[right]:
                nums[left] = nums[right]
                ll.append(nums[left])
                left += 1

        return left 
        
        
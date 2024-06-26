class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0

        n = len(nums)
        for i in range(n): 
            if nums[i] != 0: 
                nums[count] = nums[i] 
                count+=1
        
        while count < n: 
            nums[count] = 0
            count += 1
        
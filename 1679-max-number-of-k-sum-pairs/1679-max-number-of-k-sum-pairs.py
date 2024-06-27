class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i, j = 0, 1
        count = 0
        while j <= len(nums) - 1:
            if nums[i] + nums[j] == k:
                count += 1
                nums[i] = 0
                nums[j] = 0
                i += 1
                j = i + 1
            else:
                j += 1
                
        return count


        
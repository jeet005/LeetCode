class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first = sys.maxsize
        second = sys.maxsize

        for num in nums:
            if num > second:
                return True
            
            if num <= first:
                first = num
            elif num <= second:
                second = num
        
        return False
        
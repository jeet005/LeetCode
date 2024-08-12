class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict_ = {}
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            if num not in dict_:
                dict_[num] = i
        
        return [dict[i] for i in nums]

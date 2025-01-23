class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_ = []
        for i in nums:
            sorted_.append(abs(i) * abs(i))
        result = sorted(sorted_)
        return result
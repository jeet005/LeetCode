class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        res = []

        while len(nums) > 1:
            max_ = max(nums)
            min_ = min(nums)

            avg = (max_ + min_) / 2
            if avg not in res:
                res.append(avg)

            nums.remove(max_)
            nums.remove(min_)

        return len(res)
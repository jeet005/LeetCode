class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2 = set(nums1), set(nums2)

        common_digits = set1 & set2

        if len(common_digits) > 0:
            return min(common_digits)

        min_num1, min_num2 = min(nums1), min(nums2)

        return min(min_num1 * 10 + min_num2, min_num2 * 10 + min_num1)


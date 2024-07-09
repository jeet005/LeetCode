class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[], []]

        for i in set(nums1):
            if i not in set(nums2):
                ans[0].append(i)
        
        for i in set(nums2):
            if i not in set(nums1):
                ans[1].append(i)
        
        return ans
        
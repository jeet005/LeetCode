class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]
    
        for i in range(max(len(nums1), len(nums2))):
            if nums1[i] and nums1[i] not in nums2:
                if nums1[i] not in result[0]:
                    result[0].append(nums1[i])
            
            if nums2[i] and nums2[i] not in nums1:
                if nums2[i] not in result[1]:
                    result[1].append(nums2[i])

        return result
        
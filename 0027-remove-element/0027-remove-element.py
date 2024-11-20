class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] != val:
                left += 1
            elif nums[right] == val:
                right -= 1
            elif nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        return left



                



# approach 1: create a array and keep on appending if nums[i] != val (this is wrong as we need in-place)
# approach 2: Use two prointer to achieve O(1) space complexity
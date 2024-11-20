class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        print(nums)
        return k



                



# approach 1: create a array and keep on appending if nums[i] != val (this is wrong as we need in-place)
# approach 2: Use two prointer to achieve O(1) space complexity
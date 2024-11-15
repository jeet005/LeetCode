class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
        longest, current_length = 0, 0

        for i in range(len(nums)):

            if nums[i] <= threshold:
                if current_length == 0 and nums[i] % 2 == 0:
                    current_length = 1
                elif current_length > 0 and nums[i] % 2 != nums[i - 1] % 2:
                    current_length += 1
                else:
                    if nums[i] % 2 == 0:
                        current_length = 1
                    else:
                        current_length = 0
            else:
                current_length = 0

            longest = max(longest, current_length)

        return longest
            



                
            
            
            
            

                
        
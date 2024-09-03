class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        storage = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                storage.append(count)
                count = 0

            if nums[i] == 1:
                count += 1

        if count != 0: storage.append(count)

        result = 0
        print(storage)
        n = len(storage) - 1

        if len(storage) is 1:
            return len(nums) -1

        for x in range(n):
            result = max(result, storage[x] + storage[x+1])
        
        return result
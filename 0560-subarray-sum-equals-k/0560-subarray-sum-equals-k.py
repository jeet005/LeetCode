class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_ = 0
        sum_map = defaultdict(int)  # Default dictionary to store prefix sums
        sum_map[0] = 1  # Initialize with sum 0 having 1 occurrence

        for num in nums:
            sum_ += num

            # Check if there exists a prefix sum that when subtracted gives `k`
            if sum_ - k in sum_map:
                count += sum_map[sum_ - k]

            # Update the dictionary with the current sum
            sum_map[sum_] += 1

        return count
        
            
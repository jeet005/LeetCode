class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Use a set to store distinct averages
        averages = set()

        # Bucket sort-like approach: Keep track of the frequency of elements
        max_val = max(nums)
        min_val = min(nums)
        freq = [0] * (max_val + 1)

        # Populate frequency array
        for num in nums:
            freq[num] += 1

        # Two-pointer approach: Find pairs from the smallest and largest numbers
        i, j = 0, max_val
        while i <= j:
            # Skip numbers with 0 frequency
            while i <= j and freq[i] == 0:
                i += 1
            while i <= j and freq[j] == 0:
                j -= 1

            # If valid pair exists
            if i <= j:
                # Calculate average and add to set
                avg = (i + j) / 2
                averages.add(avg)

                # Decrease frequency for both numbers
                freq[i] -= 1
                freq[j] -= 1

        # Return the number of distinct averages
        return len(averages)
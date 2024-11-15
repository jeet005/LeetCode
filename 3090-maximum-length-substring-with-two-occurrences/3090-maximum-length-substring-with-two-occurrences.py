from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        dd = defaultdict(int)  # Dictionary to store character counts
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Variable to track the maximum length

        for right in range(len(s)):
            # Increment the count of the current character
            dd[s[right]] += 1

            # Ensure the window is valid by moving the left pointer until no character exceeds 2
            if dd[s[right]] > 2:
                while dd[s[right]] > 2:
                    dd[s[left]] -= 1
                    if dd[s[left]] == 0:
                        del dd[s[left]]
                    left += 1

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
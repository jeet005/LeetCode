class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
    
        # Check characters in the current string
        unique_chars = set(s)
        for i, char in enumerate(s):
            # If a character does not have both cases in the string, split around it
            if char.swapcase() not in unique_chars:
                # Divide and conquer: solve for both parts around the invalid character
                left = Solution.longestNiceSubstring(s[:i])
                right = Solution.longestNiceSubstring(s[i+1:])
                # Return the longest nice substring found in either half
                return left if len(left) >= len(right) else right

        # If all characters are "nice," return the current substring
        return s


            
        
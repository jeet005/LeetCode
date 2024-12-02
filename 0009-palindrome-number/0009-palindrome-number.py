class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check if original matches the reversed half or its truncated version
        return x == reversed_half or x == reversed_half // 10
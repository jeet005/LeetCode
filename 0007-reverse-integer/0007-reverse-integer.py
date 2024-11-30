class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        reversed_num = 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10  # Remove the last digit
            
            # Check for overflow before updating reversed_num
            if reversed_num > (INT_MAX - digit) // 10:
                return 0  # Overflow
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num
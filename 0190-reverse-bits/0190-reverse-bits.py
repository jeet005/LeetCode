class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = format(n, '032b')  # Convert to 32-bit binary string
        reversed_binary_str = binary_str[::-1]  # Reverse the binary string
        reversed_int = int(reversed_binary_str, 2)  # Convert back to integer
        return reversed_int
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [float('inf')] * n  # Initialize with large values
        
        # Pass 1: From left to right
        prev = float('-inf')  # Initialize to a large negative value
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev
        
        # Pass 2: From right to left
        prev = float('inf')  # Initialize to a large positive value
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)
        
        return result




class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1

        while i:
            if i % 2 == 0 and i % n == 0:
                return i
            else:
                i += 1

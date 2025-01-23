class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        squares = []

        for num in nums:
            squares.append(abs(num) * abs(num))

        squares = sorted(squares)
        return squares

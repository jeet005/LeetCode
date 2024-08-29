class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        maxCandies = max(candies)
        for candy in candies:
            output.append(candy + extraCandies >= maxCandies)
        
        return output

        return output
        
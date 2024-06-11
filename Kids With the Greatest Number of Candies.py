def kidsWithCandies(candies, extraCandies):
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


result = kidsWithCandies([2,3,5,1,3], 3)
print(result)
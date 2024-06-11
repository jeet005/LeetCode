def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    output = []
    maxCandies = max(candies)
    for candy in candies:
        if int(candy + extraCandies) >= maxCandies:
            output.append('True')
        else:
            output.append('False')
    
    return output


result = kidsWithCandies([2,3,5,1,3], 3)
print(result)
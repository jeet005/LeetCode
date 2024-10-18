class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        right = len(coins) - 1
        output = []
        count_sum = 0
        while count_sum < amount:
            if (count_sum + coins[right]) <= amount:
                output.append(coins[right])
                count_sum += coins[right]
            elif (count_sum + coins[right]) > amount:
                if (right - 1) >= 0:
                    right -= 1
                else:
                    return -1
        
        return len(output)
        
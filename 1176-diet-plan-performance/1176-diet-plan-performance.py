class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        left, right = 0, k
        points = 0
        j = len(calories)
        consumed = sum(calories[left:right])
        while right <= j:
            
            if right-1 != j:
                caloriesconsumed = consumed + calories[right]
                caloriesconsumed = caloriesconsumed - calories[left]

                if caloriesconsumed < lower:
                    points -= 1
                elif caloriesconsumed > upper:
                    points += 1

            left += 1
            right += 1
            

        return points
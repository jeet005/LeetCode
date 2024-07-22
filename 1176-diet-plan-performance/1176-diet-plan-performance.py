class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        left, right = 0, k
        points = 0
        consumed = sum(calories[left:right])
        while right <= len(calories):
            
                
                if consumed < lower:
                    points -= 1
                elif consumed > upper:
                    points += 1

                if right < len(calories):
                    consumed = consumed - calories[left]
                    consumed = consumed + calories[right]


                left += 1
                right += 1
            

        return points
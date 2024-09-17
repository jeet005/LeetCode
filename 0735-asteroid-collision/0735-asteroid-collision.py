class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            
            while stack and (num > 0 and stack[-1] < 0) or stack and (num < 0 and stack[-1] > 0):
                if abs(stack[-1]) == abs(num):
                    stack.pop()
                    num = 0
                    continue
                elif abs(stack[-1]) < abs(num):
                    stack.pop()
                elif abs(stack[-1]) > abs(num):
                    num = 0
        
            if num:
                stack.append(num)
        
        return stack


        
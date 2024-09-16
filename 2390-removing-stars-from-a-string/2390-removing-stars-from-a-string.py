class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        
        for x in s:
            if x != '*':
                arr.append(x)
            elif x == '*':
                arr.pop()
        
        return ''.join(arr)

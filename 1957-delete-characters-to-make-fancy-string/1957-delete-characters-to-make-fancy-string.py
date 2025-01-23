class Solution:
    def makeFancyString(self, s: str) -> str:
        
        prev = s[0]
        freq = 1
        ans = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                freq += 1
            else:
                freq = 1
                prev = s[i]
            
            if freq < 3:
                ans += s[i]
        
        return ans

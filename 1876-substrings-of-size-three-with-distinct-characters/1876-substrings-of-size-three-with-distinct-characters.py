class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def good(sub):
            if len(set(sub)) == len(sub):
                return True
            else:
                return False

        goodstrings = []
        for i in range(len(s)):
            curr_chars = s[i: i + 3]
            if good(curr_chars):
                if len(curr_chars) == 3:
                    goodstrings.append(curr_chars)
        
        return len(goodstrings)
            
                
                
            
            

        
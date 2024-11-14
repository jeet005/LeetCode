class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def nice_string(sub):
            ss = set(sub)
            for char in sub:
                if char.swapcase() not in ss:
                    return False
            return True



        longest_str = ''
        for i in range(len(s)):
            for r in range(i+1, len(s) + 1):
                current_str = s[i:r]
                if nice_string(s[i:r]):
                    if len(current_str) > len(longest_str):
                        longest_str = current_str

        
        return longest_str


            
        
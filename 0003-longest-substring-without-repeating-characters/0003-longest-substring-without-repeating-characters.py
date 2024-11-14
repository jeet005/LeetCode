class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
            

        substring = ''
        arr = []
        for x in s:
            if x in substring:
                arr.append(substring)
                substring = x
            else:
                substring += x
        
        arr.append(substring)
        return len(max(arr, key=len))
            

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charinIndex = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in charinIndex:
                charinIndex.remove(s[l])
                l += 1
            charinIndex.add(s[r])
            ans = max(ans, r - l + 1)
        
        return ans




        
            

        
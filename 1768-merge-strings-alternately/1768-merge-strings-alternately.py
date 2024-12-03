class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0
        r = 0
        result = ''
        while l < len(word1) and r < len(word2):
            result += word1[l]
            result += word2[r]
            l += 1
            r += 1

        if l < len(word1):
            for word in word1[l:]:
                result += word
        elif r < len(word2):
            for word in word2[r:]:
                result += word

        return result
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ''
        for idx in range(max(len(word1), len(word2))):
            if idx < len(word1):
                output += word1[idx]

            if idx < len(word2):
                output += word2[idx]
        
        return output
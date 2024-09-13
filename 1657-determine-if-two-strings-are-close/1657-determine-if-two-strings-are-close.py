from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if both words have the same length
        if len(word1) != len(word2):
            return False
        
        # Initialize frequency arrays for both words (size is constant 26 for all lowercase letters)
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        # Count the frequency of each character in word1 and word2
        for char in word1:
            freq1[ord(char) - ord('a')] += 1
        for char in word2:
            freq2[ord(char) - ord('a')] += 1
        
        # Check if both words contain the same set of characters
        # A non-zero frequency in one array must correspond to a non-zero frequency in the other
        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False
        
        # Sort the frequency arrays and compare
        # Sorting two arrays of size 26 is constant time (since it's independent of input size)
        return sorted(freq1) == sorted(freq2)


        


            

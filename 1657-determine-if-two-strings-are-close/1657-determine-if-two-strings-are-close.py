from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if both words have the same length
        if len(word1) != len(word2):
            return False
        
        # Create frequency maps using Counter
        word1_map = Counter(word1)
        word2_map = Counter(word2)
        
        # Compare character sets directly (unordered comparison)
        if set(word1_map.keys()) != set(word2_map.keys()):
            return False
        
        # Compare the frequency histograms (unordered comparison)
        if Counter(word1_map.values()) != Counter(word2_map.values()):
            return False
        
        return True


        


            

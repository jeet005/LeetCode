from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        hmap1 = Counter(word1)
        hmap2 = Counter(word2)
        hmap1 = dict(sorted(hmap1.items()))
        hmap2 = dict(sorted(hmap2.items()))
        if word1 == word2:
            return True
        
        if len(word1) != len(word2):
            return False

        for key, val in hmap1.items():
            if key not in hmap2:
                return False
            
        return True

        


            

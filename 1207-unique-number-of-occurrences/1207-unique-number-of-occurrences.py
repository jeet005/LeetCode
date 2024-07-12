class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}

        for i in arr:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
            
        hmap1 = []
        for key, val in hmap.items():
            if val in hmap1:
                return False
            else:
                hmap1.append(val)
        
        return True
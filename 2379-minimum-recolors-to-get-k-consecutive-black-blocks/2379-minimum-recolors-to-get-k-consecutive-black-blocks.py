class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        def requiredCount(sub):
            res = 0
            i = 0
            while i < len(sub):
                if sub[i] != 'B':
                    res += 1
                i += 1
            
            return res

        minCount = float('inf')
        for i in range(len(blocks)):
            sub = blocks[i:i + k]
            if len(sub) == k:
                currCount = requiredCount(sub)
                minCount = min(minCount, currCount)
            else:
                break
    
        return minCount
            

        
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        l = 0
        output = 0

        while (k + l) < len(s):
            i = 0
            for x in range(l, k + l):
                if s[x] in vowels:
                    i += 1
            
            output = max(i, output)
            l += 1
        
        return output


        
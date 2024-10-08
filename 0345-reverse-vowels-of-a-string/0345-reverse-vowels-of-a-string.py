class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        start = 0
        end = len(s) - 1
        s_list = list(s)

        while start < end:

            while start < end and s_list[start] not in vowels:
                start += 1
            
            while start < end and s_list[end] not in vowels:
                end -= 1
            
            s_list[start], s_list[end] = s_list[end], s_list[start]
            
            start += 1
            end -= 1

        return ''.join(s_list)



            
        


        return output
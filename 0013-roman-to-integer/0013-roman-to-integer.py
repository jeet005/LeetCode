class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        
        res = 0
        left = 0
        while left < len(s):
            if left < len(s) - 1:
                if (s[left] == 'I' and s[left + 1] == 'V') or (s[left] == 'I' and s[left + 1] == 'X') or (s[left] == 'X' and s[left + 1] == 'L') or (s[left] == 'X' and s[left + 1] == 'C') or (s[left] == 'C' and s[left + 1] == 'D') or (s[left] == 'C' and s[left + 1] == 'M'):
                    res += dict[str(s[left] + s[left+1])] 
                    left += 2
                    continue

            res += dict[s[left]] 
            left += 1

        return res







#logic
#save the roman numbers in a dict
# before adding check for edge cases like IV, IX and other
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        total = dict[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if dict[s[i]] < dict[s[i + 1]]:
                total -= dict[s[i]]
            else:
                total += dict[s[i]]

        return total







#logic
#save the roman numbers in a dict
# before adding check for edge cases like IV, IX and other
from collections import Counter

class Solution:
    def isFascinating(self, n: int) -> bool:

        output = str(n)
        output += str(n * 2)
        output += str(n * 3)

        res = Counter(output)

        print(res)

        for i in range(1, 10):
            if str(i) not in output:
                return False

            if res[str(i)] > 1:
                return False

        return True

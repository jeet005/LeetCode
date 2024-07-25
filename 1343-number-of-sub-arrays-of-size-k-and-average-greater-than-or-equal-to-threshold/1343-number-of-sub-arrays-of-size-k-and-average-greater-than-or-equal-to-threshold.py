class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        count = 0
        summ = sum(arr[:k])
        if summ/k >= threshold:
            count += 1

        for j in range(k, len(arr)):
            summ += arr[j] - arr[i]
            i += 1

            if summ/k >= threshold:
                count += 1
            
        return count


            
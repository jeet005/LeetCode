class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i,j = 0,k
        count = 0
        summ = sum(arr[i:k])
        if summ/k >= threshold:
            count += 1

        for j in range(k, len(arr)):
            summ -= arr[i]
            i += 1
            summ += arr[j]

            if summ/k >= threshold:
                count += 1
            
        return count


            
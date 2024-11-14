class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        ans = 0;
        for x in range(len(str(num))):
            substr = str(num)[x:x+k:];
            
            if len(substr) < k: break;
            elif int(substr) == 0: continue;

            ans += num % int(substr) == 0;
        
        return ans        
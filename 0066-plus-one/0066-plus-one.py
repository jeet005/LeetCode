class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # approach 1:
        num = ''
        for x in digits:
            num += str(x)
        
        res = int(num) + 1
            
        return [int(i) for i in str(res)]
        

# approach 1: we will take all the elements and plus 1

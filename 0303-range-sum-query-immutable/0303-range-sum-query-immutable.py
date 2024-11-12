class NumArray:

    def __init__(self, nums: List[int]):
        self.numarray = nums
        self.result = []

    def sumRange(self, left: int, right: int) -> int:
        self.result = sum(self.numarray[left:right + 1])
        return self.result
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
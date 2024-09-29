class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum = float('-inf')
        c_sum = 0

        for num in nums:
            c_sum = max(num, c_sum + num)
            m_sum = max(m_sum, c_sum)

        return m_sum
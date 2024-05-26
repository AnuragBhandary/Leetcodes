class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[-1] - 1
        n = nums[-2] - 1

        return m*n

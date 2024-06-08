class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        m = max(nums)

        for i in range(k):
            total += m
            m += 1

        return total

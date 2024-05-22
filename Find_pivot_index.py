class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        total = sum(nums)
        left = 0

        if l == 0:
            return -1

        for i in range(l):
            if left == total - nums[i]:
                return i
            else:
                left += nums[i]
                total -= nums[i]
            
        return -1

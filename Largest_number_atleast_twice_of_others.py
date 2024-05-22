class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind = nums.index(max(nums))
        nums.sort()

        if nums[-1] >= 2*nums[-2]:
            return ind
        else:
            return -1

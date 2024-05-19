class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        for x in range(l-1, -1, -1):
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)

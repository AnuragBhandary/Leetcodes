class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l-1, -1, -1):
            x = nums[i]
            if x%2 != 0:
                nums.append(x)
                nums.pop(i)

        return nums

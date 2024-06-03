class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i]%6 == 0:
                res.append(nums[i])

        if len(res) == 0:
            return 0

        return sum(res)//len(res)

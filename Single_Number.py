class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}

        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else:
                res[nums[i]] = 1

        for key, value in res.items():
            if value == 1:
                return key

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = {}

        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else:
                res[nums[i]] = 1

        return [key for key, value in res.items() if value == 1]

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        numset = set(nums)

        if len(numset) == 1:
            return "equilateral"

        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            if len(numset) == 2:
                return "isosceles"
            else:   
                return "scalene"
        else:
            return "none"

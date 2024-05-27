class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in ref:
                return [i, ref[complement]]
            ref[nums[i]] = i

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])
'''

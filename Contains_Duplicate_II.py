class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ref = {}

        for i in range(len(nums)):
            if nums[i] not in ref:
                ref[nums[i]] = i
            elif i - ref[nums[i]] <=k:
                return True
            else:
                ref[nums[i]] = i

        return False

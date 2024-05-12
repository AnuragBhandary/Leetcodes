class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for j in range(0,len(nums)-1):
            if nums[j] == nums[j+1]:
                return True
                break
        
        if bool != True:
            return False

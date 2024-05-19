class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 1000

        nums.sort()
        
        for i in nums:
            if i != 1000:
                k += 1

        return k

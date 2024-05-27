class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = 0
        x = 0

        while x < 101:
            for i in range(len(nums)):
                if nums[i] >= x:
                    count += 1
            
            if count == x:
                return x
            
            count = 0
            x += 1
                 
        return -1

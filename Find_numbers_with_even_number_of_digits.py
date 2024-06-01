class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        
        for i in nums:
            i = str(i)
            if len(i)%2 == 0:
                res += 1

        return res

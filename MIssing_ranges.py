class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # count = 0
        # while lower <= count <= upper:
        res = []
        
        for num in nums:
            if num>lower:
                res.append([lower, num-1])
            lower = num + 1

        if lower <= upper:
            res.append([lower, upper])

        return res

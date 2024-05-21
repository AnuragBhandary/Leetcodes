class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        res = []
        check_set = set(nums)

        for i in range(num_len):
            if i + 1 not in check_set:
                res.append(i + 1)
        return res

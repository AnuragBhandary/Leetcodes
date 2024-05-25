class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        total = 0

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for key, value in dic.items():
            if value == 1:
                total += key

        return total

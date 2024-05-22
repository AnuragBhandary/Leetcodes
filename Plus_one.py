class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        res = []

        for i in digits:
            num += str(i)

        x = int(num) + 1

        for i in str(x):
            res.append(int(i))

        return res

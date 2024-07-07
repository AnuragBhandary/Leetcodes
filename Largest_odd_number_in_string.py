class Solution:
    def largestOddNumber(self, num: str) -> str:
        count = 0

        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2 == 1:
                return num[:len(num)-count]
            else:
                count += 1
                

        return ""

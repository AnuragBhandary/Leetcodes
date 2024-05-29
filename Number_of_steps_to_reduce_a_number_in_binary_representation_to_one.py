class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)[::-1]
        num = 0
        count = 0

        for i in range(len(s)):
            if s[i] == "1":
                num += 2**i

        while True:
            if num%2 == 0:
                num //= 2
                count += 1
            elif num == 1:
                return (count)
            else:
                num += 1
                count += 1

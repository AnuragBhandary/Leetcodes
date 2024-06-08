class Solution:
    def totalMoney(self, n: int) -> int:
        
        c = n//7

        total = c*28 + 7*c*(c-1)//2

        for i in range(1, n%7+1):
            total += c+i

        return total

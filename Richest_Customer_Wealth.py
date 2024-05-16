class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []

        for i in accounts:
            sum = 0
            for j in i:
                sum += j
                res.append(sum)
        
        res.sort()
        return(res[-1])

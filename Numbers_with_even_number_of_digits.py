class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = []
        count = 0
        div = 0
        
        for i in nums:
            i = str(i)
            for j in i:
                count += 1
            res.append(count)
            count = 0

        for x in res:
            if x%2 == 0:
                div +=1

        return div

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)

        return res

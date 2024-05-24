class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        res = []
        for i in grid:
            c = i.count(1)
            res.append(c)

        return res.index(max(res))

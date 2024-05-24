class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(len(mountain)):
            if i == 0 or i == len(mountain) - 1:
                pass
            elif mountain[i-1] < mountain[i] > mountain[i+1]:
                res.append(i)

        return res

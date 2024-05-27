class Solution:
    def reverseWords(self, s: str) -> str:
        line = s.split()
        line.reverse()
        res = []

        for i in line:
            i = list(i)
            i.reverse()
            i = "".join(i)
            res.append(i)

        res.reverse()

        return (" ".join(res))

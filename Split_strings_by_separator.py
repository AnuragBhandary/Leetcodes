class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for i in words:
            a = i.split(separator)
            for j in a:
                if j != "":
                    res.append(j)

        return res

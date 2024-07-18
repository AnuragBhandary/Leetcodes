class Solution:
    def oddString(self, words: List[str]) -> str:
        res = {}
        diff = []

        for word in words:
            for j in range(len(word)-1):
                diff.append(ord(word[j+1])-ord(word[j]))
            res[words[i]] = diff
            diff = []

        values = list(res.values())

        majority = max(values, key=values.count)

        return next(key for key, value in res.items() if value != majority)

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []

        words = set(words)

        for i in words:
            for j in range(len(text)-len(i)+1):
                if text[j:j+len(i)] == i:
                    res.append([j, j+len(i)-1])

        res.sort()

        return res

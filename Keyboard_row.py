class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiopQWERTYUIOP"
        second = "asdfghjklASDFGHJKL"
        third = "zxcvbnmZXCVBNM"
        res = []

        for word in words:
            count = 0
            for i in range(len(word)):
                if word[0] in first and word[i] in first:
                    count += 1
                elif word[0] in second and word[i] in second:
                    count += 1
                elif word[0] in third and word[i] in third:
                    count += 1
            if count == len(word):
                res.append(word)

        return res

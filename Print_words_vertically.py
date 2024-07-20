class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        words = s.split()
        longest = max(words, key=len)

        for i in range(len(longest)):
            term = ""
            for word in words:
                if i > len(word) - 1:
                    term += " "
                else:
                    term += word[i]

            term = term.rstrip()

            res.append(term)

        return res

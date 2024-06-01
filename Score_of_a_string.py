class Solution:
    def scoreOfString(self, s: str) -> int:
        words = list(s)
        score = 0

        for i in range(len(words)-1):
            score += abs(ord(words[i+1]) - ord(words[i]))

        return score

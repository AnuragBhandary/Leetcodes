class Solution:
    def reverseWords(self, s: str) -> str:
        line = s.split()
        line.reverse()

        return " ".join(line)

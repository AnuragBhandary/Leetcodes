class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = len(searchWord)

        s = sentence.split()

        for i in range(len(s)):
            if s[i][:l] == searchWord:
                return i+1

        return -1

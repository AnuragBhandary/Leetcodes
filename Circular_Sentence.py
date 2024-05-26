class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        c = 0 

        if len(words) == 1:
            if words[0][0] == words[0][-1]:
                return True

        for i in range(len(words)-1):
            if words[i][-1] == words[i+1][0] and words[0][0] == words[-1][-1]:
                c = 1
            else:
                c = 0
                break

        if c == 1:
            return True

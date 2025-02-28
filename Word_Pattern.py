class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False

        ch2w = {}
        w2ch = {}

        for char, word in zip(pattern, words):
            if char in ch2w and ch2w[char] != word:
                return False
            if word in w2ch and w2ch[word] != char:
                return False

            ch2w[char] = word
            w2ch[word] = char

        return True

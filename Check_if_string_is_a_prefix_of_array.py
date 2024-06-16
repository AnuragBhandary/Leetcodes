class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l = len(s)
        a = "".join(words)

        if s == a:
            return True

        if l < len(words[0]):
            return False
        
        for i in words:
            if i in s:
                s = s[len(i):]
            elif s == "":
                return True
            else:
                return False

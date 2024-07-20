class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char = list(chars)
        res = ""
        good = True

        for word in words:
            for i in word:
                if i not in char:
                    good = False
                    break
                else:
                    char.remove(i)
            if good == True:
                res += word
            good = True
            char = list(chars)

        return len(res)

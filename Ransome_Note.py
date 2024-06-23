class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Complexity O(m)
        if len(ransomNote)>len(magazine):
            return False

        letters = collections.Counter(magazine)

        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1

        return True

        
        # MY SOLUTION WORKED!! Complexity = O(m+n)
        # x = list(ransomNote)
        # y = list(magazine)

        # if len(y) < len(x):
        #     return False

        # try:
        #     for i in range(len(x)):
        #         y.pop(y.index(x[i]))
        # except:
        #     return False

        # return True

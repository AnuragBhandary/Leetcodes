class Solution:
    def longestPalindrome(self, s: str) -> int:
        ref = {}
        res = 0
        odd = False

        for i in s:
            if i in ref:
                ref[i] += 1
            else:
                ref[i] = 1
            
        val = [val for val in ref.values()]

        for i in val:
            if i%2 != 0:
                odd = True
            if i>1:
                res += i//2

        if odd == True:
            return res*2 + 1
        else:
            return res*2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ref = {}
        count = 0

        for i in s:
            if i in ref:
                ref[i] += 1
            else:
                ref[i] = 1

        if min(ref.values()) > 1:
            return -1
        else:
            return s.index(min(ref, key=ref.get))  

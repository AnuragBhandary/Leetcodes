class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False

        if s1 == s2:
            return True
        
        count = 0

        for i, j in zip(s1, s2):
            if i != j:
                count += 1

        if count!=2:
            return False
        
        return True

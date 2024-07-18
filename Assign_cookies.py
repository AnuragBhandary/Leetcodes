# NEED A BETTER SOLUTION 
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort()
        l = len(g)
        

        for i in range(l-1, -1, -1):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    s.pop(j)
                    g.pop(i)
                    break

        return l - len(g)

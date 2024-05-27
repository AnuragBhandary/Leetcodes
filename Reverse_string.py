class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        #s.reverse()

        '''
        l = len(s)
        for i in range(len(s)-1, -1, -1):
                s.insert(-1, s[i])

        for i in range(l-1):
            s.pop(0)

        s.pop()
        '''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = list(''.join(ch for ch in s if ch.isalnum()))
        j = -1

        for i in range(len(a)//2):
            if a[i] == a[j]:
                j -= 1
            else:
                return False
                
        return True

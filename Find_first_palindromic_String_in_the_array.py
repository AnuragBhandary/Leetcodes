class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # for word in words:
        #     if word == word[::-1]:
        #         return word

        # return ""

        def palindrome(word):
            start = 0
            end = len(word) - 1

            while start <= end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1

            return True

        for word in words:
            if palindrome(word):
                return word

        return ""

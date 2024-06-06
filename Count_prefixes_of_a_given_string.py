class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for i in words:
            l=len(i)
            if s[:l] == i:
                count=count+1
        return count
        
        ''' SOLVED 122/123 TEST CASES '''
        # count = 0

        # for i in words:
        #     if i[0] == s[0]:
        #         if i in s:
        #             count += 1

        # return count

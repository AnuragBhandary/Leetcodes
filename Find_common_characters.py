class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        comm = True
        first = words[0]

        for i in first:
            for j in range(len(words)):
                if comm == True:
                    if i in words[j]:
                        words[j] = words[j].replace(i, '', 1)
                    else:
                        comm = False

            if comm == True:
                res.append(i)
            
            comm = True
            
        return res

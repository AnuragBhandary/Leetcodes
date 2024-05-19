class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = high
            high = max(high, temp)
        arr[-1] = -1
        return arr
        
        
        
        '''res = []
        for i in range(len(arr)):
            arr[i] = 0
            m = max(arr)
            if m != 0:
                res.append(m)
            else:
                res.append(-1)

        return res'''

        '''res = []
        i = 0
        for x in range(i, len(arr)):
            arr.pop(0)
            if arr != []:
                m = max(arr)
                res.append(m)
                i += 1
            else:
                res.append(-1)

        return res'''
        
        '''if not arr or len(arr) == 1:
            return [-1]
        res = []
        l = len(arr)
        for i in range(l-1):
            res.append(max(arr[i+1:l]))
        res.append(arr[-1])
        res[-1] = -1
        return res'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)

        for i in range(l-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i+1, 0)

        for i in range(len(arr), -1, -1):
            if l == len(arr):
                return arr
            else:
                arr.pop()

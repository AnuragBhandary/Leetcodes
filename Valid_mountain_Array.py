class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        
        if l < 3:
            return False
        
        top = max(arr)

        top_id = arr.index(top)
        if top_id == l-1 or top_id == 0:
            return False
            
        for i in range(1, top_id):
            if arr[i] <= arr[i-1]:
                return False

        for i in range(top_id, l-1):
            if arr[i] <= arr[i+1]:
                return False

        return True 

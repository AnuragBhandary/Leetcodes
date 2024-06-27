# Time and Space Complexity = O(1)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0], edges[1]

        if first[0] in second:
            return first[0]
        else:
            return first[1] 

# Time Complexity = O(N+M)
# import statistics
# from statistics import mode

# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         res = []
#         for i in edges:
#             for j in i:
#                 res.append(j)

#         return mode(res)
                

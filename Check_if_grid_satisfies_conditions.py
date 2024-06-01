class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i > 0 and grid[i][j] != grid[i - 1][j]:
                    return False
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    return False

        return True
        
        
        # m = len(grid[0])
        # n = len(grid)
        # mark = False

        # if m == n == 1:
        #     return True
        # elif n == 1:
        #     for i in range(m-1):
        #         if grid[0][i] != grid[0][i+1]:
        #             mark = True
        #         else:
        #             return False
        #     return True
        
        # if m == 1:
        #     for i in range(n-1):
        #         if grid[i][0] == grid[i+1][0]:
        #             mark = True
        #         else:
        #             return False
            

        # for i in range(n-1):
        #     for j in range(m-1):
        #         if grid[i][j] == grid[i+1][j] and grid[i][j] != grid[i][j + 1]:
        #             mark = True
        #         else:
        #             return False


        #         if grid[i][-1] == grid[i+1][-1] and grid[i][-2] != grid[i][-1]:
        #             mark = True
        #         else:
        #             return False

        # if mark == True:
        #     return True
        # else:
        #     return False

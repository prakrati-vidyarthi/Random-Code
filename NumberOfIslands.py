from collections import defaultdict
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        num_islands, visited = 0, defaultdict(bool)
        rows, columns = len(grid), len(grid[0])
        
        def is_valid(i, j):
            if (i >= 0 and i < rows and j >= 0 
                and j < columns and not visited[(i,j)]
                and grid[i][j] == "1"):
                return True
            return False
        
        def dfs(i, j):
            if not is_valid(i,j):
                return 
            visited[(i, j)] = True
            paths = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in paths:
                dfs(i+dx, j+dy)
        
        for i in range(rows):
            for j in range(columns):
                if (not visited[(i, j)] and 
                    grid[i][j] == "1"):
                    dfs(i, j)
                    num_islands += 1
        return num_islands

###################
### 200. Number of Islands
### Given an m*n 2D binary grid which represents a map of
### '1's (land) and '0's (water), return the number of
### islands.

### An island is surrounded by water is formed by connecting
### adjacent lands horizontally or vertically. You may assume
### all four edged of the grid are surrounded by water.
###################

######################### PROBLEM COVERS #########################
# DEPTH-FIRST SEARCH (DFS)
# BREADTH-FIRST SEARCH (BFS)
# RANGE(LEN())

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # helper function using depth-first search (DFS)
        # visits all connected '1's (land)
        def dfs(i, j):
            # stopping condition - stop if conditions are true: 
                # i < 0 = going above top row - out of bounds
                # i >= len(grid) = going below last row - out of bounds
                # j < 0 = going left of first column - out of bounds
                # j >= len(grid[0]) = going right of last column - out of bounds
                # grid[i][j] == '0' = reached water (or already sinked)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # marking land as visited by 'sinking' it in water
            grid[i][j] = '0'

            # exploring all 4 directions of each list item
            dfs(i+1, j) # checking down
            dfs(i-1, j) # checking up
            dfs(i, j+1) # checking right
            dfs(i, j-1) # checking left

        islands = 0

        # looping through every item in grid
        for i in range(len(grid)): # i = current row
            for j in range(len(grid[0])): # j = current column
                # if the i(row), j(column) index/value = 1 (land)
                if grid[i][j] == '1':
                    # do the helper function that sinks the island
                    dfs(i, j) # sink whole island
                    islands += 1 # count this as one full island

        # return the number of total islands
        return islands


                
                


s = Solution()
answer = s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(answer)
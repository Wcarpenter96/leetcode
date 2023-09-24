from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # If a cell has 1 adjacent cell it has 3 walls
        # If a cell has 2 adjacent cells it has 2 walls
        # ...
        walls = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    walls += 4
                    # check for laterally surrounding island
                    if j > 0 and row[j - 1] == 1:
                        walls -= 1
                    if j < len(row)-1 and row[j + 1] == 1:
                        walls -= 1
                    # check for vertically surrounding island
                    if i > 0 and grid[i - 1][j] == 1:
                        walls -= 1
                    if i < len(grid)-1 and grid[i + 1][j] == 1:
                        walls -= 1
        return walls


test1 = Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
print(test1)

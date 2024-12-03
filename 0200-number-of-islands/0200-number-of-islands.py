class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        island = 0

        def dfs(grid, r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1"):
                return

            grid[r][c] = "0"

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    island += 1


        return island
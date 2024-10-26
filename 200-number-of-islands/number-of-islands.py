class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    stack = [(i, j)]
                    grid[i][j] = '0'  # Mark as visited
                    while stack:
                        r, c = stack.pop()
                        for x, y in [(r - 1, c), (r + 1, c), (r, c -1), (r, c + 1)]:
                            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                                stack.append((x, y))
                                grid[x][y] = '0'
        return num_islands
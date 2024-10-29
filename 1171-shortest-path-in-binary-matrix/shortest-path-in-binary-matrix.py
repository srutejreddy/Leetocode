class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] != 0 or grid[N-1][N-1] != 0: return -1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1 
        
        while queue:
            row, col, path_length = queue.popleft()
            
            if row == N - 1 and col == N - 1:
                return path_length
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < N and 0 <= new_col < N and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, path_length + 1))
                    grid[new_row][new_col] = 1 
        
        return -1

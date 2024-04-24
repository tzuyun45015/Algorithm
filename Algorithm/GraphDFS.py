class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0
        
        def DFS(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or 
                grid[r][c] == 0):
                return 0
            visit.add((r,c))
            return (1 + DFS(r + 1, c) +
                        DFS(r - 1, c) +
                        DFS(r, c + 1) +
                        DFS(r, c - 1))
            
        for r in range(rows):
            for c in range(cols):
                    area = max(area, DFS(r,c))
        return area

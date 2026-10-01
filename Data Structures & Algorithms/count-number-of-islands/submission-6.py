class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(r, c):
            visit.add((r, c))
            q = deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in visit
                    and grid[nr][nc] == "1"):
                            visit.add((row + dr, col + dc))
                            q.append((row + dr, col + dc))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    islands += 1

        return islands
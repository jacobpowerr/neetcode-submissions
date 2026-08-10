class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.pop()
                for dc, dr in directions:
                    r, c = (row + dr), (col + dc)
                    if (r < len(grid) and c < len(grid[0])
                    and r >= 0 and c >= 0 and grid[r][c] == "1"
                    and (r, c) not in visit):
                        visit.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    visit.add((r, c))

        return islands
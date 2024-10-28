from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()
            if min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1:
                continue
            if r == N -1 and c == N - 1:
                return length
            for d in direct:
                if (r + d[0], c + d[1]) not in visited:
                    q.append((r + d[0], c + d[1], length + 1))
                    visited.add((r + d[0], c + d[1]))
        return -1
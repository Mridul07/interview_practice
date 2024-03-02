class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (self.explore(grid, r, c, visited) == True):
                    count += 1

        return count
                
        
    def explore(self, grid, r, c, visited):
        rowBound = 0 <= r and r < len(grid)
        colBound = 0 <= c and c < len(grid[0])
        if (not rowBound or not colBound):
            return False
        
        if grid[r][c] == "0":
            return False

        if (str(r) + ',' + str(c)) in visited:
            return False
        visited.add(str(r) + ',' + str(c))

        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)

        return True
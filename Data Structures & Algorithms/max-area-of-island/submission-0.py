class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j): #returns the area of island and explores the whole island
            queue = [(i, j)]
            area = 1

            while queue:
                (i, j) = queue.pop(0)

                if i + 1 < rows and grid[i + 1][j] == 1 and (i + 1, j) not in visited:# explore right
                    area += 1
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
                if i - 1 > -1 and grid[i - 1][j] == 1 and (i - 1, j) not in visited:# explore left
                    area += 1
                    queue.append((i - 1, j))
                    visited.add((i - 1, j))
                if j + 1 < cols and grid[i][j + 1] == 1 and (i, j + 1) not in visited:# explore up
                    area += 1
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))
                if j - 1 > -1 and grid[i][j - 1] == 1 and (i, j - 1) not in visited:# explore down
                    area += 1
                    queue.append((i, j - 1))
                    visited.add((i, j - 1))
            
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:

                    visited.add((i, j))
                    area = bfs(i, j)
                    maxArea =  max(area, maxArea)
        
        return maxArea







        
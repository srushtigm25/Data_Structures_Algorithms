class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS way 

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def dfs(r, c):
            #out of bounds
            if r< 0 or r >= rows or c< 0 or c>=cols:
                return 

            #Water or Already visited
            if grid[r][c] == "0":
                return 

            #Mark as visted
            grid[r][c] = "0"

            #Explore 4 neighbors

            dfs(r-1, c) #up
            dfs(r+1, c) #down
            dfs(r, c-1) #left
            dfs(r, c+1) #right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

            
            



        
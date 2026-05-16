class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        num=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                size=self.traverse(i,j,grid,visited)
                if size >0:
                    num+=1
        return num

    def traverse(self, i, j, grid, visited):
        if i<0 or i >= len(grid) or j < 0 or j>= len(grid[i]):
            return 0
        if visited[i][j]:
            return 0
        visited[i][j]=True
        if grid[i][j] == '0':
            return 0
        return (1 + 
        self.traverse(i+1, j, grid, visited) + 
        self.traverse(i-1, j, grid, visited) + 
        self.traverse(i, j+1, grid, visited) + 
        self.traverse(i, j-1, grid, visited) )
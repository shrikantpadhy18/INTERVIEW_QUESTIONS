class Solution:
    def minPathSum(self, grid: List[List[int]],m=0,n=0) -> int:
        dp=[[0]*len(grid[0])]*len(grid)
        dp[0][0]=grid[0][0]
        for i in range(1,len(grid)):
            grid[i][0]+=grid[i-1][0]
        for j in range(1,len(grid[0])):
            grid[0][j]+=grid[0][j-1]
            
        print(grid)
            
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
                
        return(grid[len(grid)-1][len(grid[0])-1])
import numpy as np
n=int(input("enter the number of rows:"))
dp=np.array([]*n*n)
vis=np.zeros([n,n],dtype=int)
dp.resize(n,n)
def ways(row,column,n):
  if row==n-1 and column==n-1:
    dp[row][column]=1
    vis[row][column]=1
    return 1
  if row==n-1 :
    if vis[row][column+1]==1:
      return dp[row][column+1]
    else:
      dp[row][column+1]=ways(row,column+1,n)
      vis[row][column+1]=1
      return dp[row][column+1]
  if column==n-1:
    if vis[row+1][column]==1:
      return dp[row+1][column]
    else:
      dp[row+1][column]=ways(row+1,column,n)
      vis[row+1][column]=1
      return dp[row+1][column]
  else:
    if vis[row][column+1]==1:
      x=dp[row][column+1]
    else:
      x=ways(row,column+1,n)
      dp[row][column+1]=x
      vis[row][column+1]=1
    if vis[row+1][column]==1:
      y=dp[row+1][column]
    else:
      y=ways(row+1,column,n)
      dp[row+1][column]=y
      vis[row+1][column]=1
      
    return(x+y)
print(ways(0,0,n))

import numpy as np
def output(x,y):
  if mat[x,y]==1:
    dp[x,y]=1
    vis[x,y]=1
    return 1
  else:
    ans=1000
    for i in range(rows):
      if x!=i and mat[x,i]==1:
        if vis[i,y]==1:
          ans =min(ans,mat[x,i]+dp[i,y])
        else:
          dp[i,y]=output(i,y)
          vis[i,y]=1
          ans=min(ans,mat[x,i]+dp[i,y])
            
            
    return ans

rows=int(input("enter the number of colors a chameleon can changed into" ))
length=rows*rows
dp=np.array([0]*length,dtype=int)
dp.resize(rows,rows)
print(dp)
vis=np.zeros([rows,rows],dtype=int)
print(vis)
ls=list(map(int,input("Enter the list of elements of 1s and 0s").split()))
mat=np.array(ls)
mat.resize(rows,rows)
print(mat)
if len(ls)==length:
  print(output(0,3))
else:
  print("You Have Entered  Insufficient Data,Try Again")

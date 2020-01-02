
def fun(m,n):
  if m==3 and n==3:
    return mat[m][n]
  elif m==3 and n<3:
    return mat[m][n]+fun(m,n+1)
  elif n==3 and m<3:
    return mat[m][n]+fun(m+1,n)
  else:
    return mat[m][n]+max(fun(m+1,n),fun(m,n+1))


mat=[list(map(int,input("Enter 4 space separated integers denoting number of coins at each particular cells").split())) for i in range(4) ]
print(fun(0,0))

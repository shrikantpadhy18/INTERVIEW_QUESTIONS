from collections import Counter
st=input()
ls=list(st)
k=int(input())
cs=Counter(ls)
print(cs)
if True:
  m=0
  for i,j in cs.items():
    if j%2!=0 and k>0:
      cs[i]-=1
      k-=1
  print(cs)
  for i in cs.values():
    if i%2!=0:
      m+=1
  print(m)
  if(m==1 or m==0):
    print("PALINDROME")
  
  else:
    
    print("NON PALINDROME")

    
  

from collections import Counter
ls=list(map(int,input().split()))
ans=0
result=0
for i in range(0,len(ls)):
  for j in range(len(ls)-1,-1,-1):
    if(i<j and max(Counter(ls[i:j+1]).values())<2 and len(ls[i:j+1])>ans):
      ans=len(ls[i:j+1])
      result=ls[i:j+1]
print(ans," ",result)

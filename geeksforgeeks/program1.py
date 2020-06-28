from math import *
k=int(input())
for i in range(k):
    n=int(input())
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    for i in range(2,int(sqrt(n))+1):
        j=2
        if(prime[i]==True):
            while(i*j<=n):
                prime[i*j]=False
                j+=1
    ls=[]
    for i in range(len(prime)):
        if prime[i]==True:
            ls.append(i)
    start=0
    end=len(ls)-1
    while(end>start):
        if(ls[start]+ls[end]==n):
            print(ls[start],end=" ")
            print(ls[end])
            break
        elif(ls[start]+ls[end]<n):
            start+=1
        elif(ls[start]+ls[end]>n):
            end-=1
            
    
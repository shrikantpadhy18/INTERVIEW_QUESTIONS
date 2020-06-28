from math import *

prime=[True]*(1000000)
    #print(prime)
prime[0]=False
prime[1]=False
for i in range(2,int(sqrt(100000))):
    j=2
    if prime[i]==True:
        while i*j<=100000:
            prime[i*j]=False
            j+=1
k=int(input())
for t in range(k):
    l,h=map(int,input().split())          
    for i in range(l,h+1):
        if(prime[i]==True):
            print(i,end=" ")
    
    print()   
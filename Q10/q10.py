d={
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
su=0
s=input()
for i in range(len(s)-1,-1,-1):
  if(i==len(s)-1):
    su+=d[s[i]]
  elif(d[s[i]]<d[s[i+1]]):
    su-=d[s[i]]
  else:
    su+=d[s[i]]

print(su)

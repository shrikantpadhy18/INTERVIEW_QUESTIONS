w=input("Enter the string:")
res=[]
for i in range(len(w)):
  for j in range(i+1,len(w)):
    c=w[i:j+1]
    if c==c[::-1] and all(len(c)>=len(t) for t in res):
      res.append(c)
s=0
name=None
for i in res:
  if len(i)>s:
    s=len(i)
    name=i
print(res)
print("The max length palindrome is :{}".format(name))

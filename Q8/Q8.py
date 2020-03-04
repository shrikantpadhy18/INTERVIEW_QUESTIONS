from itertools import permutations
s= "dogcatcatcodecatdog"
word=["cat","dog"]
permute=[]
for i in range(2,len(s)):
  permute.extend(permutations(word,i))
result=[]
print(permute)
for i in permute:
  result.append("".join(i))

result1=[]
try:
  for i in result:
    result1.append(s.index(i))
  print(result1)
except:
  print(result1)

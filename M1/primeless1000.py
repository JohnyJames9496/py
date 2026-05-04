count = 0
print(2,end=" ")
for i in range(3,1000):
  for j in range(2,i):
    if i%j==0:
      break
  else:
    print(i,end=" ")
    count +=1
print(count)
N=int(input())
ct=0
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if i==3 or j==3 or k==3:
        ct+=1
print(ct)
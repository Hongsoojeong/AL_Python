N=int(input())
ct=0
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        #만약 23시 59분 28초라면 => 235928 로 된다
        ct+=1
print(ct)
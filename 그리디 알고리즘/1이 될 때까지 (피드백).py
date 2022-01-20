N,K=map(int,(input().split()))
ct=0
while N>=K: 
  if N<K:
    while N%K!=0:
      N-=1
      ct+=1
  else:
    N=N//K
    ct+=1
print(ct)

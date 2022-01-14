def sol_1(N):
  ct=0
  while N!=1:
    N=N-1
    ct+=1
  return ct

def sol_2(N,K):
  ct=0
  while N!=1:
    N=N//K
    ct+=1
  return ct

N,K=map(int,(input().split()))
print(min(sol_1(N),sol_2(N,K)))
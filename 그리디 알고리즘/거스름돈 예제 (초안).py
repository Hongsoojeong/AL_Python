
N=int(input()) # 남은 돈
n=0
while N//500>0:
  N-=500
  n+=1
while N//100>0:
  N-=100
  n+=1
while N//50>0:
  N-=50
  n+=1
while N!=0:
  N-=10
  n+=1
print(n) # 최소 동전 개수 
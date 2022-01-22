N,M=map(int,input().split())
n,m,actor=input().split()
map=list()
for i in range(0,N):
  a=list(input().split())
  map.append(a)
current='1'
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1 
# 1 1 1 1
# 서쪽은 [j][i+1]
# 남쪽은 [j+1][i]
# 북쪽은 [j-1][i]
# 동쪽은 [j][i-1]
step=0
i=int(n)
j=int(m)
ct=0
while current!='0':
  print(i,j)
  if ct==3:
    i=0
    j-=1
    if map[j][i]=='0':
      break
  if map[j][i]!='Done':
    map[j][i]='Done'
  else:
    i-=1
    ct+=1
  
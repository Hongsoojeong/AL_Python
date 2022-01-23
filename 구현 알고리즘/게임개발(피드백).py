
N,M=map(int,input().split())

d= [[0]*M for _ in range(N)]
x,y,direction=map(int,input().split())
d[x][y]=1

gmap=list()
for i in range(N):
  gmap.append(list(map(int,input().split())))

dx=[-1,0,1,0] #북동남서
dy=[0,1,0,-1]

def turn_left():
  global direction
  direction-=1 
  if direction == -1: #전부 돌았을 경우
    direction=3

ct=1
turn_ct=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]
  # 회전한 후 안 가본 칸에 이동한다
  if d[nx][ny]==0 and gmap[nx][ny]==0:
    d[nx][ny]=1
    x=nx
    y=ny
    ct+=1
    turn_ct=0
    continue
  else:
    turn_ct+=1
  
  if turn_ct==4:
    nx=x-dx[direction]
    ny=y-dy[direction]
    if gmap[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_ct=0

print(ct)    
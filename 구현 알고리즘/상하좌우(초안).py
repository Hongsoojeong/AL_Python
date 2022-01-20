N=int(input()) # 공간의 크기 N
path=input().split() # 이동할 경로
row=1 #행
col=1 #열
for i in range (0,len(path)):
  if path[i]=="L": #열을 한칸 이동
    if col==1:
      continue # 공간밖은 무시
    col-=1
  elif path[i]=="R": #열을 한칸 이동
    if col==N:
      continue
    col+=1
  elif path[i]=="U": #행을 한칸 이동
    if row==1:
      continue
    row-=1
  else: #path[i]=="D" #행을 한칸 이동
    if row==N:
      continue
    row+=1
print(row,col)
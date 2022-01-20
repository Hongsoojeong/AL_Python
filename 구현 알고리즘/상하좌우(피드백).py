N=int(input()) # 공간의 크기 N
path=input().split() # 이동할 경로
row=1 #행
col=1 #열
move_types_row=[0,0,-1,1]
move_types_col=[-1,1,0,0]
path_types=["L","R","U","D"]

for plan in path:
  for i in range(len(path_types)):
    if plan==path_types[i]:
      nr=row+move_types_row[i]
      nc=col+move_types_col[i]
  if nr>N or nr<1 or nc>N or nc<1:
    continue
  row=nr
  col=nc
print(row,col)
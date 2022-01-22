coor=input() #좌표
row=int(coor[1]) 
col=int(ord(coor[0]))-int(ord('a'))+1 
#a:1, b:2 ...
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
ct=0
for step in steps:
  next_row=row+step[0]
  next_column=col+step[1]
  if next_row >=1 and next_row<=8 and next_column>=1 and next_column<=8:
    ct+=1
print(ct)
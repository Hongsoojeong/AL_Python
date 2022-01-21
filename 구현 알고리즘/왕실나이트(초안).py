coor=input() #좌표

coor_row=coor[0] #열 (a~h)
coor_col=coor[1] #행 (1~8)
ct=0

row=['a','b','c','d','e','f','g','h']
col=[1,2,3,4,5,6,7,8]

right_row1=[1,1,1,1,1,1,1,0]
right_row2 = [2,2,2,2,2,2,0,0]

left_row1=[0,-1,-1,-1,-1,-1,-1,-1]
left_row2 =[0,0,-2,-2,-2,-2,-2,-2]

down_col1=[1,1,1,1,1,1,1,0]
down_col2 = [2,2,2,2,2,2,1,0]

up_col1=[0,-1,-1,-1,-1,-1,-1,-1]
up_col2=[0,0,-2,-2,-2,-2,-2,-2]

for i in row:
  if coor_row==i: #(a~h)
    for j in col:
      if int(coor_col)==j: #(1~8)
        if not i in ['a','b','g','h']:
          if not j in [1,2,7,8]:
            ct=8
          else:
            if j==1:
              ct=4
            elif j==2:
              ct=6
            elif j==7:
              ct=6
            elif j==8:
              ct=4
        else:
          if i=='a' or i=='h':
            if not j in [1,2,7,8]:
              ct=4
            else:
              if j==1:
                ct=2
              elif j==2:
                ct=3
              elif j==7:
                ct=3
              elif j==8:
                ct=2
          else:
            if not j in [1,2,7,8]:
              ct=4
            else:
              if j==1:
                ct=3
              elif j==2:
                ct=4
              elif j==7:
                ct=4
              elif j==8:
                ct=3
        break
print(ct)    
    
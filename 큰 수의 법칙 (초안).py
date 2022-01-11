size,N,M=list(map(int, input().split()))  # 배열의 크기, 더하는 횟수,최대 횟수 
x=list(map(int, input().split())) 
x.sort()
x_max=x[-1]
x_second_max=x[-2]
answer=0
count=0
while N!=0:
  if count==M:
    answer+=x_second_max
    count=0
    N-=1
  else:
    answer+=x_max
    count+=1
    N-=1
print(answer)
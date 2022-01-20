n,m,k=list(map(int, input().split()))  # 배열의 크기, 더하는 횟수,최대 횟수 
x=list(map(int, input().split())) 
x.sort()
x_max=x[-1]
x_second_max=x[-2]
answer=0

count=int(m/(k+1))*k #가장 큰 수가 더해지는 계산
count+=m%(k+1)

answer+= count*x_max
answer+=(m-count)*x_second_max
print(answer)

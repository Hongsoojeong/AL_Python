N,M=map(int,(input().split()))
card=list()
#result=0 책 풀이
for n in range(0,N):
  row=list(map(int,(input().split())))
  card.append(min(row))
  # min_value=min(row) 책 풀이
  #result=max(result,min_value) 책 풀이
print(max(card))
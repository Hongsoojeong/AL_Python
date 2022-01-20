N,M=map(int,(input().split()))
card=list()
for n in range(0,N):
  row=list(map(int,(input().split())))
  card.append(row)

min_card=list()
for n in range(0,N):
  min_card.append(min(card[n]))
print(max(min_card))
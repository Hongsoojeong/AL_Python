N=int(input())
coin_types=[500,100,50,10]
count=0
for coin in coin_types:
  count+=N//coin
  N%=coin 
print(count)
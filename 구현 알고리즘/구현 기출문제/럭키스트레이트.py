def cal(score):
  score=str(score)
  length=len(score)
  middle=length//2
  sum1=0
  sum2=0
  for i in range(0,middle):
    sum1+=int(score[i])
  for j in range(middle,length):
    sum2+=int(score[j])
  if sum1==sum2:
    return True
  else:
    return False

score=int(input())
if cal(score):
  print("LUCKY")
else:
  print("READY")
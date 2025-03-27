num=int(input())
f=(num//10**9)%10
t=(num//10**7)%10
l=num%10
tl=(num//10**2)%10
sum=f+l+t+tl
if sum%3==0:
  print("code sucess")
else:
  print("failure")

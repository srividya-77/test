num=input()
f=int(num[0])
t=int(num[2])
l=int(num[-1])
tl=int(num[-3])
sum=l+t+l+tl
if sum%3==0:
  print("code sucess")
else:
  print("code failure")

t1,t2=raw_input().split()
t1=int(t1)
t2=int(t2)
for n in range(t1,t2):
  sum=0
  temp=n
  while temp > 0:
    digit=temp%10
    sum+=digit ** 3
    temp//=10
  if n==sum:
    print(n)

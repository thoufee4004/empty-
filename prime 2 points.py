t,t1=raw_input().split()
t=int(t)
t1=int(t1)
for num in range(t+1,t1):
	if num > 1:
          for i in range(2,num):
                 if (num % i) == 0:
                          break
          else:
                 print num,

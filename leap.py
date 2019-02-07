while True:
	try:
		t1=int(input())
		break
	except:
		print('invalid')
		break
if t1%400==0 or t1%4==0 or t1%100!=0:
	print('yes')
else:
	print('no')

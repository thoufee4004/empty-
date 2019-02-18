while True:
	try:
		a,b=raw_input('\n').split()
		a=int(a)
		b=int(b)
		if(raw_input>0):
			print "start",a, "end",b
			km=b-a
			print 'total km=',km
			print("1.micro" '\n' "2.mini" '\n' "3.premium" '\n')
			key=int(input('enter types'))
			if key==1:
			 print("fare=", km*10)
			 break
			 if key==2:
			 	print("fare=", km*15)
			 break
			 if key==3:
			 	print("fare=", km*20)
			 break
	
	except:
		print("invalid input")
		break

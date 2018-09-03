print("check whether a number is odd or even")
a=int(input("enter the number"))
print(a)
if(a==0):
    print('the given input is zero')
elif(a%2!=1):
    print('the given number',+a,'is even')
elif(a%2==1):
 print('the given number',+a,'is odd')
else:
    print('the given input is not valid')

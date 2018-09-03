list =['a','e','i','o','u','A','E','I','O','U']
a=raw_input("enter the input")
print(a)
if a.isdigit():
 print('the input',a,"is a integer input")
else:
 if(a in list):
  print('the input',a,'is a vowel letter')
 else:
    print('the input',a,'is not a vowel')

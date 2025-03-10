def toplama(x, y):
  print (x+y)
def cikarma (x, y):
  print (x-y)
def bolme(x, y):
  print (x/y)
def carpma(x, y):
  print (x*y)
  
operator=input("Operation:")
x=int(input("Zahl1="))
y=int(input("Zahl2="))
if operator=="+":
  toplama(x,y)
elif operator=="-":
  cikarma(x,y)
elif operator=="/":
  bolme(x,y)
elif operator=="*":
  cikarma(x,y)
else:
  print("Bitti")

 
 
  
  
a=int(input("enter number1"))
b=int(input("enter number2"))
c=int(input("enter number3"))
d=(b**2)-4*a*c
print(d)
if d>0:
  print("there are two real roots")
elif d==0:
  print("there is one real root")
else:
  print("there are two complex roots")


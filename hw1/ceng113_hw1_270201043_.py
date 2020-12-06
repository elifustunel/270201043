eq1= open('inputs_1.txt')
eq1=str(input("Enter the first equation:\n"))
eq2=str(input("Enter the second equation:\n"))

xk=[]
xkn=[]
yk=[]
ykn=[]
xm=[]
xmn=[]
ym=[]
ymn=[]
k=str()
n=str()
m=str()
l=str()
e=0
for g in range(0,len(eq1)):
  if eq1[g]=="=":
    k=str(eq1[0:g])
    l=(eq1[g+1:])
for h in range(0,len(eq2)):
  if eq2[h]=="=":
    m=(eq2[0:h])
    n=(eq2[h+1:])
    
for  i in range(0,len(k)) :
  if (k[i] == 'x') :
    if k[i-2]=="+":
      e=int(k[i-1])
      xk.append(e)
    elif k[i-3]=="+":
      e=int(k[i-2]+k[i-1])
      xk.append(e)
    
for  i in range(0,len(k)) :
  if (k[i] == 'x') :
    if k[i-2]=="-":
      e=int(k[i-1])
      xkn.append(e) 
    elif k[i-3]=="-":
      e=int(k[i-2]+k[i-1])
      xkn.append(e)
for  i in range(0,len(k)) :          
  if (k[i] == 'y') :
    if k[i-2]=="+":
      e=int(k[i-1])
      yk.append(e)
    elif k[i-3]=="+":
      e=int(k[i-2]+k[i-1])
      yk.append(e)
for  i in range(0,len(k)) :
  if (k[i] == 'y') :
    if k[i-2]=="-":
      e=int(k[i-1])
      ykn.append(e) 
    elif k[i-3]=="-":
      e=int(k[i-2]+k[i-1])
      ykn.append(e)
for  i in range(0,len(l)) :
  if (l[i] == 'x') :
    if  l[i-2]=="+":
      e=int(l[i-1])
      xkn.append(e)
    elif l[i-3]=="+":
      e=int(l[i-2]+l[i-1])
      xkn.append(e)
for  i in range(0,len(l)) :
  if (l[i] == 'x') : 
    if l[i-2]=="-":
      e=int(l[i-1])
      xk.append(e) 
    elif l[i-3]=="-":
      e=int(l[i-2]+l[i-1])
      xk.append(e)
for  i in range(0,len(l)) :
  if (l[i] == 'y') :
    if  l[i-2]=="+":
      e=int(l[i-1])
      ykn.append(e)
    elif l[i-3]=="+":
      e=int(l[i-2]+l[i-1])
      ykn.append(e)
for  i in range(0,len(l)) :
  if (l[i] == 'y') :
    if l[i-2]=="-":
      e=int(l[i-1])
      yk.append(e) 
    elif l[i-3]=="-":
      e=int(l[i-2]+l[i-1])
      yk.append(e)  
for  i in range(0,len(m)) :

  if (m[i] == 'x') :
    if  m[i-2]=="+":
      e=int(m[i-1])
      xm.append(e)
    elif m[i-3]=="+":
      e=int(m[i-2]+m[i-1])
      xm.append(e)
for  i in range(0,len(m)) :
  if (m[i] == 'x') : 
    if m[i-2]=="-":
      e=int(m[i-1])
      xmn.append(e) 
    elif m[i-3]=="-":
      e=int(m[i-2]+m[i-1])
      xmn.append(e)
for  i in range(0,len(m)) :
  if (m[i] == 'y') :
    if  m[i-2]=="+":
      e=int(m[i-1])
      ym.append(e)
    elif m[i-3]=="+":
      e=int(m[i-2]+m[i-1])
      ym.append(e)
for  i in range(0,len(m)) :
  if (m[i] == 'y') :
    if m[i-2]=="-":
      e=int(m[i-1])
      ymn.append(e) 
    elif m[i-3]=="-":
      e=int(m[i-2]+m[i-1])
      ymn.append(e)
for  i in range(0,len(n)) :
  if (n[i] == 'x') :
    if  n[i-2]=="+":
      e=int(n[i-1])
      xmn.append(e)
    elif n[i-3]=="+":
      e=int(n[i-2]+n[i-1])
      xmn.append(e)
for  i in range(0,len(n)) :
  if (n[i] == 'x') : 
    if n[i-2]=="-":
      e=int(n[i-1])
      xm.append(e) 
    elif n[i-3]=="-":
      e=int(n[i-2]+n[i-1])
      xm.append(e)
for  i in range(0,len(n)) :
  if (n[i] == 'y') :
    if  n[i-2]=="+":
      e=int(n[i-1])
      ymn.append(e)
    elif n[i-3]=="+":
      e=int(n[i-2]+n[i-1])
      ymn.append(e)
for  i in range(0,len(n)) :
  if (n[i] == 'y') :
    if n[i-2]=="-":
      e=int(n[i-1])
      ym.append(e) 
    elif n[i-3]=="-":
      e=int(n[i-2]+n[i-1])
      ym.append(e)


nx1=0
for i in xk:
    nx1+=i
ny1=0
for i in yk:
    ny1+=i
nxn1=0
for i in xkn:
    nxn1+=i
nyn1=0
for i in ykn:
    nyn1+=i
nx2=0
for i in xm:
    nx2+=i
ny2=0
for i in ym:
    ny2+=i
nxn2=0
for i in xmn:
    nxn2+=i
nyn2=0
for i in ymn:
    nyn2+=i
a=int(nx1)-int(nxn1)
b=int(ny1)-int(nyn1)
o=int(nx2)-int(nxn2)
p=int(ny2)-int(nyn2)
if b>=0:
  b="+"+str(b)
if p>=0:
  p="+"+str(p)

print("Equations in the simplified form:")
print(str(a)+"x"+str(b)+"y"+"="+"c")
print(str(o)+"x"+str(p)+"y"+"="+"s")

print("Solution:")
print("x=",)
print("y=",)
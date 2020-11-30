eq1=str(input("Enter the first equation:\n"))
eq2=str(input("Enter the second equation:\n"))

nx=[]
ny=[]
nc=[]
p1=[]
p2=[]
e=0


for g in range(0,len(eq1)):
  if eq1[g]=="=":
    p1.append(eq1[0:g])
  
  if eq1[g]=="=":
    p2.append(eq1[g+1:])
p2=str(p2)    
for h in range(0,len(p2)):
  if p2[h]=="+" :
    p2=p2.replace("+","-") 




for  i in range(0,len(p1)):
  if (p1[i] == 'x'): 
    if p1[i-2]=="+":
      e="+"+p1[i-1]
      nx.append(e)

  if (p1[i] == 'x') : 
    if p1[i-2]=="-":
      e="-"+p1[i-1]
      nx.append(e) 

  if (p1[i] == 'y') : 
    if p1[i-2]=="+":
      e="+"+p1[i-1]
      ny.append(e)

  if (p1[i] == 'y') : 
    if p1[i-2]=="-":
      e="-"+p1[i-1]
      ny.append(e) 


print(p1)
print(p2)
print(nx)
print(ny)

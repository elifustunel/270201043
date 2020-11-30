eq1=str(input("Enter the first equation:\n"))
eq2=str(input("Enter the second equation:\n"))

l1=len(eq1)
l2=len(eq2)
nx=[]
ny=[]
nc=[]
e=0

for i in range(0,l1):  
  
  if (eq1[i] == '=') :    
    if (eq1[i+3] == 'x'): 
     if eq1[i+1]=="+":
      e="-"+eq1[i+2]
     nx.append(e)

    elif (eq1[i+3] == 'x') : 
     if eq1[i+1]=="-":
      e="+"+eq1[i+2]
      nx.append(e) 

    elif (eq1[i+3] == 'y') : 
     if eq1[i+1]=="+":
      e="-"+eq1[i+2]
      ny.append(e)

    elif (eq1[i+3] == 'y') : 
     if eq1[i+1]=="-":
      e="+"+eq1[i+2]
    



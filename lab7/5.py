p=input("Enter password:")
l=0
u=0
d=0 
for i in p: 
  if (i.islower()): # counting lowercase alphabets 
   l+=1           
  if (i.isupper()):   # counting uppercase alphabets 
    u+=1            
  if (i.isdigit()):   # counting digits 
    d+=1            
           
if l>=1 and u>=1 and  d>=1 and len(p)>=8:
    print("Valid Password") 
else: 
    print("Invalid Password") 
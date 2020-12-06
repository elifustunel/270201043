email_address=input("enter your email address:")
x="ceng113@example.com"

email_address=email_address.lower()
for i in range(len(email_address)):
  if email_address[i]=="@":
    l=email_address[i:]
    k=email_address[0:i]
    k=k.replace(".","")
email_address=k+l 
if x==email_address:
    print(True)
else:
    print(False)
 

  
   
    














  

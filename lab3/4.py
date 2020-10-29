age=int(input("enter age:"))
ticket=3

if 6>age or 60<age :
  print(ticket*0)

elif 6<age<18  :
  print(ticket*50/100)

else:
  print(ticket)


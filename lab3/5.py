day=int(input("enter day"))
month=int(input("enter month"))

if (month==3 and day>=20) or (month==4 or month==5) or (month==6 and day<21):
  print("spring")

elif (month==6 and day>=21) or (month==7 or month==8) or  (month==9 and day<22):
  print("summer")

elif (month==9 and day>=22) or (month==10 or month==11) or (month==11 and day<21):
  print("fall")

else:
  print("winter")
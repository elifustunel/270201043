GPA=float(input("GPA"))
number_of_lecture=int(input("number of lecture"))

if GPA<2.0 and number_of_lecture<47:
  print("not enough number of lecture & GPA")

elif GPA<2.0 and number_of_lecture>=47:
   print("not enough GPA")

elif GPA>=2.0 and number_of_lecture<47:
    print("not enough number of lecture")

elif GPA>=2.0 and number_of_lecture>=47:
   print("GRADUATED!!")

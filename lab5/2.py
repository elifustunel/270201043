N = int(input("How many numbers?"))
even = 0
for i in range(N):
  i = int(input("Please enter an integer:"))
  if i % 2 == 0:
   even += 1
print("%", even/N*100)